#%%
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\src\数据分析\DataAnalysis\pandas\dogNames2.csv")

df[(800 < df["Count_AnimalName"]) & (df["Count_AnimalName"] < 1000)]

# df["info"].split("\").tolist()


t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))
t3
t3.iloc[1:,:2] = np.nan

pd.isnull(t3)
pd.notnull(t3)
t3

t3.dropna(axis=0)

d2 = {
    "name": ["xiaoming", "xiaohong", "xiaogang"],
    "age": [20,10, 20],
    "tel": [100,300, 400]
}

pd.DataFrame(d2)

# d2.mean()
# d2["age"].fillna(d2["age"].mean())
d2["age"][1] = np.nan
d2["name"][0] = np.nan
pd.DataFrame(d2)

d2["age"].mean()

