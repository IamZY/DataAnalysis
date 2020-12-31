import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from linear_regression import LinearRegression

data = pd.read_csv('../data/world-happiness-report-2017.csv')

# 得到训练和测试数据
train_data = data.sample(frac = 0.8)
test_data = data.drop(train_data.index)

input_param_name = 'Economy..GDP.per.Capita.'
output_param_name = 'Happiness.Score'

x_train = train_data[input_param_name].values
y_train = train_data[output_param_name].values

x_test = test_data[input_param_name].values
y_test = test_data[output_param_name].values


plt.scatter(x_train,y_train,label='Train data')
plt.scatter(x_test,y_test,label='Test data')
plt.xlabel(input_param_name)
plt.ylabel(output_param_name)
plt.title('Happy')
plt.legend()
plt.show()