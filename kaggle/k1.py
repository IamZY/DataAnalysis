import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("fivethirtyeight")
import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv("train.csv")
print(data.head())

# 统计缺失值 计算每一列缺失多少数据
print(data.isnull().sum())

# 计算均值 只有数值型的才能算均值 不是的直接过滤
print(data.describe())

# 一行两列的子图
# ax[0] 左边的图
# figsize 18*8
f,ax = plt.subplots(1,2,figsize=(18,8))
# 分别计数
data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived',data=data,ax=ax[1])
ax[1].set_title('Survived')
# plt.show()

# plt.savefig('./t1.png')

#
print(data.groupby(['Sex','Survived'])['Survived'].count())

f,ax = plt.subplots(1,2,figsize=(18,8))
data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax=ax[0])
# 分别计数
ax[0].set_title('Survived')
sns.countplot('Sex',hue='Survived',data=data,ax=ax[1])
ax[1].set_title('Sex:Survived va Dead')
# plt.show()

print(pd.crosstab(data.Pclass,data.Survived,margins=True).style.background_gradient(cmap='summer_r'))
# pd.show_versions()

sns.factorplot('Pclass','Survived',hue='Sex',data=data)
# plt.show()

# 连续值对结果的影响
print('Oldest Passenger was of:',data['Age'].max(),'Years')

# 小提琴图
f,ax = plt.subplots(1,2,figsize=(18,8))
sns.violinplot('Pclass','Age',hue='Survived',data=data,split=True,ax=ax[0])
# 分别计数
ax[0].set_title('Pclass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
sns.violinplot('Sex','Age',hue='Survived',data=data,split=True,ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0,110,10))
# plt.show()


# 缺失值填充
#   + 平均值
#   + 经验值
#   + 回归模型预测
#   + 删除掉

data['Initial']=0
for i in data:
    data['Initial']=data.Name.str.extract('([A-Za-z]+)\.')

print(pd.crosstab(data.Initial,data.Sex).T.style.background_gradient(cmap='summer_r'))


print(data.groupby('Initial')['Age'].mean())

## 使用每组的均值来进行填充
data.loc[(data.Age.isnull())&(data.Initial=='Mr'),'Age']=33
data.loc[(data.Age.isnull())&(data.Initial=='Mrs'),'Age']=36
data.loc[(data.Age.isnull())&(data.Initial=='Master'),'Age']=5
data.loc[(data.Age.isnull())&(data.Initial=='Miss'),'Age']=22
data.loc[(data.Age.isnull())&(data.Initial=='Other'),'Age']=46

print(data.Age.isnull().any()) #看看填充完了咋样


f,ax=plt.subplots(1,2,figsize=(20,10))
data[data['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',color='red')
ax[0].set_title('Survived= 0')
x1=list(range(0,85,5))
ax[0].set_xticks(x1)
data[data['Survived']==1].Age.plot.hist(ax=ax[1],color='green',bins=20,edgecolor='black')
ax[1].set_title('Survived= 1')
x2=list(range(0,85,5))
ax[1].set_xticks(x2)
plt.show()


