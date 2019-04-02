# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 加载数据
# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
# df = pd.read_csv('./source_data/AA00004.csv', parse_dates=['location_time'], date_parser=dateparse)

# 画出速度与acc状态之间的联系（散点图）
# plt.scatter(df["gps_speed"],df["acc_state"])
# plt.xlabel('速度')
# plt.ylabel('acc状态')


# 画出速度随时间变化的曲线（曲线图）
# l1 = pd.date_range(pd.datetime.strptime('1998-02-17', '%Y-%m-%d'),
#                   pd.datetime.strptime('2019-04-02', '%Y-%m-%d'), freq='M')


# print(l1)
# plt.xticks(l1, rotation=45)
# plt.plot(df['location_time'], df['gps_speed'])

# plt.plot(['l','j','c','sad','dsd'],[1,2,3,3,4])
# plt.xticks(['l','j','c','dsd'],['l1','1j','1c','1dsd'])

# plt.plot([1,2,3,5],[1,2,3,5])
# plt.xticks([1,2,5],['a','b','c'])

x = [pd.datetime.strptime('1998-02-17', '%Y-%m-%d'),pd.datetime.strptime('1998-02-18', '%Y-%m-%d'),pd.datetime.strptime('1998-02-19', '%Y-%m-%d'),pd.datetime.strptime('1998-02-21', '%Y-%m-%d')]
plt.plot(x,[1,2,3,4])


# 最后显示画图结果
plt.show()

print(pd.datetime)
print(pd.DataFrame)