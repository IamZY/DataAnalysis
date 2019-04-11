#%%
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\src\数据分析\DataAnalysis\pandas\dogNames2.csv")

df.head()
df.info()

df.sort_values(by="Count_AnimalName",ascending=False)[:10]

# Series
df["Row_Labels"]

t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))

t3.loc["a", "z"]
t3.loc["a", :]

t3.iloc[[1, 2]]

t3.iloc[:, [2, 3]]

t3

t3.iloc[:,3] = 1

t3
