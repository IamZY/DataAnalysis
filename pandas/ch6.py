#%%
import pandas as pd
import numpy as np
food_info = pd.read_csv(r"D:\src\数据分析\DataAnalysis\pandas\food_info.csv")
# print(type(food_info))
# print(food_info.dtypes)

# 显示前五条数据
# print(food_info.head())
# print(food_info.head(3))

# print(food_info.columns)
# 维度
# print(food_info.shape)
# 切片从那开始到哪结束
# print(food_info.loc[3])

ndb_col = food_info["NDB_No"]
# print(ndb_col)

# columns = ["", ""]
# x = food_info[columns]

col_names = food_info.columns.tolist()
# print(col_names)
gram_cols = []

for c in col_names:
    if c.endswith("(g)"):
        gram_cols.append(c)

gram_df = food_info[gram_cols]
# print(gram_df)

# 排序
# food_info.sort_values("",inplace=True,ascending=False)

titanic_surival = pd.read_csv(
    r"D:\src\数据分析\DataAnalysis\pandas\titanic_train.csv")

# print(titanic_surival.head())

ages = titanic_surival["Age"]
# print(ages)
age_is_null = pd.isnull(ages)
# print(age_is_null)
# print(ages[age_is_null])

good_ages = titanic_surival["Age"][age_is_null == False]
# print(good_ages)

corrent_age = titanic_surival["Age"].mean()
# print(corrent_age)

# print(titanic_surival[titanic_surival["Pclass"] == 1].head())

passenger_survival = titanic_surival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)

print(passenger_survival)

port_stats = titanic_surival.pivot_table(index="Embarked", values=["Fare", "Survived"], aggfunc=np.sum)
print(port_stats)

# drop

Pclass_Series = titanic_surival["Pclass"]
print(type(Pclass_Series))


