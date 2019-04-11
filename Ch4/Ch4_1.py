#%%
import pandas as pd
import os
df1 = pd.DataFrame({'sku': ['a', 'a', 'e', 'c'], 'data': [1, 1, 2, 3]})
df2 = pd.DataFrame({'sku': ['a', 'b', 'f']})
df3 = pd.DataFrame({'sku': ['a', 'b', 'd']})
df4 = pd.DataFrame({'sku': ['a', 'b', 'c', 'd']})
print(pd.merge(df2, df1))


data_folder = os.path.join(
    os.getcwd(), "数据分析\DataAnalysis\Ch4\data", "data")
# print(data_folder)

# print(os.getcwd())
ratings_filename = os.path.join(data_folder, "u.data")

def user_action_check():
    df_user = pd.read_csv(data_folder+'/JData_User.csv', encoding='gbk')
    df_sku = df_user.loc[:, 'user_id'].to_frame()
    df_month2 = pd.read_csv(data_folder+'/JData_Action_201602.csv', encoding='gbk')
    print('Is action of Feb. from User file? ', len(
        df_month2) == len(pd.merge(df_sku, df_month2)))
    df_month3 = pd.read_csv(data_folder+'/JData_Action_201603.csv', encoding='gbk')
    print('Is action of Mar. from User file? ', len(
        df_month3) == len(pd.merge(df_sku, df_month3)))
    df_month4 = pd.read_csv(data_folder+'/JData_Action_201604.csv', encoding='gbk')
    print('Is action of Apr. from User file? ', len(
        df_month4) == len(pd.merge(df_sku, df_month4)))


# user_action_check()


