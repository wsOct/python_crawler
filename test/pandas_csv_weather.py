import pandas as pd

data=pd.read_csv('data/weather.csv')
# print(data)
# 改变数据行的索引 inplace=True在原来数据的基础上修改
# 将日期作为行索引
data.set_index('日期',inplace=True)
data.index.name = None
# print(data)
#利用字符串的替换操作replace
data.loc[:, '最高温度'] = data['最高温度'].str.replace('°C', '').astype('int32')
data.loc[:, '最低温度'] = data['最低温度'].str.replace('°C', '').astype('int32')
# data.loc[:, ['最低温度','最低温度']] = data['最低温度'].str.replace('°C', '').astype('int32')
# print(data)

# 输出全年最高温度那一天信息 ascending=True升序
#首先根据最高温度降序排列，排列之后取第一行即可
result=data.sort_values(by='最高温度', ascending=False)
#输出以最高温度排序后的所有数据
# print(result)
#取第一行，也就是最高温度那一天的所有信息
# print(result.iloc[0, :])

#获取指定日期的最高和最低温度
# print(data.loc[['2023/1/3','2023/1/4','2023/1/5'],['最高温度','最低温度']])
# #最高温度大于32的所有信息
# print(data.loc[data['最高温度']>32])
# # 最高温度小于30 ，最低温度>20的所有信息
# print(data.loc[(data['最高温度']<30)&(data['最低温度']>20)])

# 查询1月的所有数据
#首先要从日期中找到1月的日期
# index_list = data.index.tolist()
# # i.startswith("2019/9") -> bool True ,False  找到以字符串‘2019/9’开头的日期，是9月的返回的就是True
# result = [i.startswith("2023/1") for i in index_list]  #遍历index_list,找到所有以"2019/9"开头的
# print(data.loc[result,:]) #这样就找到了所有的9月份数据

# 添加一列，温差
data.loc[:,'温差'] = data['最高温度'] - data['最低温度']
print(data)

# 温差>=10 ,大温差  <10 为正长
data.loc[:,'温差类型'] = ['大温差' if value>=10 else '正常' for value in data['温差']]
# print(data)

# 全年里面有多少天是正常温差
#分组
print(data.loc[:,'温差类型'].value_counts())

# 排序，根据温差数据降序排序
# print(data.sort_values(by='温差',ascending=False))
#两个条件，排序
# print(data.sort_values(by=['最高温度','温差'],ascending=False))
# print(data.sort_values(by=['最高温度','温差'],ascending=[False,True]))



