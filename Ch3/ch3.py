#%%
import pandas as pd
# dataset = pd.read_csv(
    # 'D:\src\数据分析\DataAnalysis\Ch3\data\leagues_NBA_2014_games_games.csv')
data_path = 'D:\src\数据分析\DataAnalysis\Ch3\data\leagues_NBA_2014_games_games.csv'


# dataset.ix[:5]

dataset = pd.read_csv(data_path, parse_dates=["Date"], skiprows=[0,])
dataset.columns = ["Date", "Score Type", "Visitor Team",
                   "VisitorPts", "Home Team", "HomePts", "OT?", "Notes"]

dataset.ix[:5]


dataset["HomeWin"] = dataset["VisitorPts"] < dataset["HomePts"]

dataset.ix[:5]

y_true = dataset["HomeWin"].values
print(y_true)

dataset["HomeLastWin"] = False
dataset["VisitorLastWin"] = False


from collections import defaultdict
won_last = defaultdict(int)

for index, row in dataset.iterrows():
    home_team = row["Home Team"]
    visitor_team = row["Visitor Team"]
    row["HomeLastWin"] = won_last[home_team]
    row["VisitorLastWin"] = won_last[visitor_team]
    dataset.ix[index] = row
    # Set current win
    won_last[home_team] = row["HomeWin"]
    won_last[visitor_team] = not row["HomeWin"]

dataset.ix[20:25]


from sklearn.tree import DecisionTreeClassifier
# 平均交叉检验
from sklearn.cross_validation import cross_val_score
import numpy as np

clf = DecisionTreeClassifier(random_state=14)
# 通过这两个标准值来检测比赛的正确率
x_previouswins = dataset[["HomeLastWin", "VisitorLastWin"]].values

print(x_previouswins)

scores = cross_val_score(clf, x_previouswins, y_true, scoring="accuracy")
# 准确率
print("Accuracy : {0:.1f}%".format(np.mean(scores) * 100))


import os

standings_filename = "D:\src\数据分析\DataAnalysis\Ch3\data\standings.csv"
# skiprows跳过哪些行
standings = pd.read_csv(standings_filename,skiprows=[0])

standings

dataset["HomeTeamRanksHigher"] = 0

# dataset
for index, row in dataset.iterrows():
    home_team = row["Home Team"]
    visitor_team = row["Visitor Team"]
    if home_team == "New Orleans Pelicans":
        home_team = "New Orleans Hornets"
    elif visitor_team == "New Orleans Pelicans":
        visitor_team = "New Orleans Hornets"
    home_rank = standings[standings["Team"] == home_team]["Rk"].values[0]
    visitor_rank = standings[standings["Team"] == visitor_team]["Rk"].values[0]
    row["HomeTeamRanksHigher"] = int(home_rank > visitor_rank)
    dataset.ix[index] = row

x_homehigher = dataset[["HomeLastWin", "VisitorLastWin", "HomeTeamRanksHigher"]]

clf = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(clf, x_homehigher, y_true, scoring="accuracy")
print("Accuracy : {0:.1f}%".format(np.mean(scores) * 100))


last_match_winner = defaultdict(int)
dataset["HomeTeamWonLast"] = 0

for index, row in dataset.iterrows():
    home_team = row["Home Team"]
    visitor_team = row["Visitor Team"]
    teams = tuple(sorted([home_team, visitor_team]))
    row["HomeTeamWonLast"] = 1 if last_match_winner[teams] == row["Home Team"] else 0
    dataset.ix[index] = row
    winner = row["Home Team"] if row["HomeWin"] else row["Visitor Team"]
    last_match_winner[teams] = winner

# dataset

X_home_higher = dataset[["HomeTeamRanksHigher", "HomeTeamWonLast"]].values
clf = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(clf, X_home_higher, y_true, scoring='accuracy')
print("Using whether the home team is ranked higher")
print("Accuracy: {0:.1f}%".format(np.mean(scores) * 100))


from sklearn.preprocessing import LabelEncoder
encoding = LabelEncoder()

encoding.fit(dataset["Home Team"].values)

home_teams = encoding.transform(dataset["Home Team"].values)
visitor_teams = encoding.transform(dataset["Visitor Team"].values)

X_teams = np.vstack([home_teams, visitor_teams]).T

from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder()

X_teams_expanded = onehot.fit_transform(X_teams).todense()
clf = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(clf, X_teams_expanded, y_true, scoring='accuracy')
print("Accuracy: {0:.1f}%".format(np.mean(scores) * 100))

from sklearn.ensemble import RandomForestClassifier

# 更换分类器
clf = RandomForestClassifier(random_state=14)
scores = cross_val_score(clf, X_teams, y_true, scoring='accuracy')
print("Using full team labels is ranked higher")
print("Accuracy: {0:.1f}%".format(np.mean(scores) * 100))

# hstack水平方向堆叠
X_all = np.hstack([X_home_higher, X_teams])
clf = RandomForestClassifier(random_state=14)
success = cross_val_score(clf, X_all, y_true, scoring="accuracy")
print("Accuracy: {0:.1f}%".format(np.mean(success) * 100))

# 调整最佳参数
from sklearn.grid_search import GridSearchCV

parameter_space = {
    "max_features": [2, 10, 'auto'],
    "n_estimators": [100, ],
    "criterion": ["gini", "entropy"],
    "min_samples_leaf": [2, 4, 6],
}
clf = RandomForestClassifier(random_state=14)
grid = GridSearchCV(clf, parameter_space)
grid.fit(X_all, y_true)
print("Accuracy: {0:.1f}%".format(grid.best_score_ * 100))
print(grid.best_estimator_)


