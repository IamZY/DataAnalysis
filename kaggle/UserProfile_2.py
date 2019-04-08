import pandas as pd

#编码转换完成的数据，取的是1W的子集
trainname = './data/user_tag_query.10W.TRAIN-1w.csv'
testname = './data/user_tag_query.10W.TEST-1w.csv'

data = pd.read_csv(trainname,encoding='gbk')
print (data.info())

#分别生成三种标签数据（性别，年龄，学历）
data.age.to_csv("./data/train_age.csv", index=False)
data.Gender.to_csv("./data/train_gender.csv", index=False)
data.Education.to_csv("./data/train_education.csv", index=False)
#将搜索数据单独拿出来
data.QueryList.to_csv("./data/train_querylist.csv", index=False)

data = pd.read_csv(testname,encoding='gbk')
print (data.info())

data.QueryList.to_csv("./data/test_querylist.csv", index=False)