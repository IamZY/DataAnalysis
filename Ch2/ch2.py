#%%
# from PIL import Image
import os
import numpy as np
import csv

# print(os.path.expanduser('~'))

# data_folder = os.path.expanduser('~')
# parent_path = os.path.dirname('Data')
# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
data_path = 'D:/src/数据分析/DataAnalysis/Ch2/Data/ionosphere.data'

# print(data_path)

x = np.zeros((351, 34), dtype='float')
y = np.zeros((351,) , dtype='bool')

with open(data_path, 'r') as input_file:
    reader = csv.reader(input_file)
    # print(reader.line_num)
    for i, row in enumerate(reader):
        data = [float(datum) for datum in row[:-1]]
        x[i] = data
        y[i] = row[-1] == 'g'

# print(x)
# print(y)


# im = Image.open('D:/src/数据分析/DataAnalysis/Ch2/Data/IMG_1524.jpg')
# im.show()


# 创建训练集和测试集
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=14)

from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier()
estimator.fit(X_train, y_train)

y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print("The accuracy is {0:.1f}%".format(accuracy))

from sklearn.cross_validation import cross_val_score

scores = cross_val_score(estimator, x, y, scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("The average accuracy is {0:.1f}%".format(average_accuracy))

avg_scores = []
all_scores = []

parameter_values = list(range(1, 21))
for n_neighbors in parameter_values:
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(estimator, x, y, scoring='accuracy')
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)

print(avg_scores)
print(all_scores)

# matplotlib inline
from matplotlib import pyplot as plt
plt.plot(parameter_values, avg_scores, '-o')


x_broken = np.array(x)
x_broken[:, ::2] /= 10

estimator = KNeighborsClassifier()
original_scores = cross_val_score(estimator, x, y, scoring='accuracy')
print('The original average accuracy for is {0:.1f}%'.format(np.mean(original_scores) * 100))
broken_scores = cross_val_score(estimator, x_broken, y, scoring='accuracy')
print('The "broken" average accuracy for is {0:.1f}% '.format(np.mean(broken_scores) * 100))

from sklearn.preprocessing import MinMaxScaler
x_transformed = MinMaxScaler().fit_transform(x)

print(x_transformed)