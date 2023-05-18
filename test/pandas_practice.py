import pandas as pd
import numpy


'''
Series
'''
# a = [1, 2, 3]
# myvar = pd.Series(a)
# print(myvar)
# 根据索引值读取数据
# print(myvar[1])

# 指定索引值
# str = ['google', 'facebook', 'github']
# mystr = pd.Series(str, index=["x", "y", "z"])
# print(mystr)

# 使用 key/value 对象，类似字典来创建 Series
# sites = {1: 'google', 2: 'tencent', 3: 'baidu'}
# mysites = pd.Series(sites, name="myname")
# print(mysites)


'''
DataFrame
# '''
# [[行内容]]
# data = [['google', 12], ['facebook', 13], ['win', 14]]
# df = pd.DataFrame(data, columns=['site', 'age'], dtype=float)
# print(df)

# ndarrays 创建
# {列名：列内容}
# data_item = {'Sites': ['google', 'facebook', 'win'], 'Age': [12, 13, 14]}
# df2 = pd.DataFrame(data_item)
# print(df2)
# # 数据
# print(df2.values)
# # 行名称
# print(df2.index)
# # 列名称
# print(df2.columns)

# 使用字典（key/value），其中字典的 key 为列名
# 多个字典
# shit = [{'a': 1, 'b': 2}, {'a': 5, 'b': 3, 'c': 2}]
# df3 = pd.DataFrame(shit)
# print(df3)
# loc属性返回指定行的数据
# print(df3.loc[0])
# 返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开
# 返回第一行和第二行的数据
# print(df3.loc[[0, 1]])
# loc[行名称，列名称]
# df.loc[df['A'] =='a', "B"] * 100  # 当列A中某行的值等于“a”时，B列的值乘以100
# df.loc[:,'C']  # 选取第C列的数据
# pd.to_numeric(df["A"]) # 将某一列的数据转换成数值型
# df.loc[df['A'] > 0, :]  # 取A列大于0的行
# print(df3.loc[0:0, 'a'])


'''
读取csv文件内容
'''
# df = pd.read_csv('data/confid_reuse.csv')
# print(df)
# # to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，
# # 则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
# print(df.to_string())

'''
将dataframe转储为csv文件
'''
# nme = ["Google", "Baidu", "Taobao", "Wiki"]
# # st = ["www.google.com", "www.Baidu.com", "www.taobao.com", "www.wikipedia.org"]
# # ag = [90, 40, 80, 98]
# # dict = {'name': nme, 'site': st, 'age': ag}
# # df2 = pd.DataFrame(dict)
# print(df2)
# df2.to_csv('data/site.csv')


# head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行
# print(df.head(6))
# tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。
# print(df.tail())
# info() 方法返回表格的一些基本信息
# print(df.info())


'''
数据清洗
'''
# 处理缺失
# 判断是否缺失
# stud_data=pd.Series(['张三','李四',numpy.nan,[],'',None,'王五'])
# print(stud_data)
# print(stud_data.isnull())
# print(stud_data.notnull())

# stud_df=pd.DataFrame(stud_data,columns=['student_name'])
# print(stud_df)
# print(stud_df.isnull())
# print(stud_df.notnull())

# 处理重复
# 判断重复
data=pd.DataFrame({'key1':['A','B']*3+['B'],'key2':[1,1,2,3,3,4,4]})
print(data)
print(data.duplicated())
# 删除重复
dedup_data = data.drop_duplicates()
print(dedup_data)
