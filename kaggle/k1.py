import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("fivethirtyeight")
import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv("train.csv")
print(data.head())