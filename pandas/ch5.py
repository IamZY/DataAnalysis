#%%
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv(r"D:\src\数据分析\DataAnalysis\pandas\IMDB-Movie-Data.csv")

df.head(1)
df.info()

# 准备数据
runtime_data = df["Runtime (Minutes)"].values
runtime_data


max_minutes = runtime_data.max()
min_minutes = runtime_data.min()

max_minutes
min_minutes

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(runtime_data, (max_minutes - min_minutes) // 5)

plt.xticks(range(min_minutes, max_minutes + 5, 5))

plt.show()