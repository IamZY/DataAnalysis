#%%
import pandas as pd

pd.Series([1, 2, 32, 12, 3, 4])
t = pd.Series([1, 2, 32, 12, 3, 4])

type(t)

t2 = pd.Series([1, 2, 4, 45, 5], index=list("abcde"))
t2

temp_dict = {"name": "xiaohong", "age": 30, "tel": 100086}

t3 = pd.Series(temp_dict)
t3

import string

a = {string.ascii_uppercase[i]: i for i in range(10)}
a

t3.dtype
pd.Series(a)

t3["age"]
t3[2]

t3[[1, 2]]
t3[["name", "tel"]]

t[t > 2]

t3.values

type(t3.values)

t.where(t > 1, 10)



