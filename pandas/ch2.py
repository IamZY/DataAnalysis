#%%
import pandas as pd
import numpy as np

df = pd.read_csv("D:\src\数据分析\pandas\dogNames2.csv")

df

pd.DataFrame(np.arange(12).reshape(3, 4),index=list("abc"),columns=list("WXYZ"))

d1 = {
    "mame": ["xiaoming", "xiaohong", "xiaogang"],
    "age": [10, 10, 20],
    "tel" : [200,300,400]
}

pd.DataFrame(d1)

d2 = [
    {"name": "xiaoming", "age": 20, "tel": 10086},
    {"name": "xiaohong", "tel": 3000},
    {"name": "xiaofang", "age": 30}
]

pd.DataFrame(d2)


df = pd.read_csv(r"D:\src\数据分析\pandas\train.csv")
# type(df)
df.head()
df.tail()
df.info()
df.describe()