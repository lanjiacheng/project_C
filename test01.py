# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 加载数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv('source_datas/AA00004.csv', parse_dates=['location_time'], date_parser=dateparse)

# 画出速度与acc状态之间的联系（散点图）
# plt.scatter(df["gps_speed"],df["acc_state"])
# plt.xlabel('速度')
# plt.ylabel('acc状态')


# 画出acc状态和时间之间的关系（散点图）
# plt.plot(df["location_time"],df["acc_state"])
# plt.xlabel("时间")
# plt.ylabel("acc状态")

# 查看个字段的分布
# x = range(df.shape[0])
# x = df['location_time']
# y = df['mileage']
#
# plt.xlim(xmin=df['location_time'][0],xmax=df['location_time'][df.shape[0]-1])
# plt.scatter(x,y,s=0.1,edgecolors='r')


# 根据经度纬度画出轨迹图

# df.set_index('location_time')
# plt.scatter(df['lng'],df['lat'],s=0.1)

index_pairs = []

for i in range(df.shape[0] - 1):
    df1 = df.iloc[i]
    df2 = df.iloc[i + 1]
    if df2['location_time'].timestamp() - df1['location_time'].timestamp() > 10 * 60:
        index_pairs.append([i, i + 1])
    print(i)

print(index_pairs)

split_dfs = []
start_index = 0
i = 0
len_of_paris = len(index_pairs)
for index_pair in index_pairs:
    split_df = df.iloc[start_index:index_pair[0] + 1]
    split_dfs.append(split_df)
    start_index = index_pair[1]
    if i == len_of_paris - 1:
        split_df = df.iloc[start_index:]
        split_dfs.append(split_df)
    i = i + 1

# 画图前应该将经纬度统一标准化

for split_df in split_dfs:
    plt.scatter(split_df['lng'],split_df['lat'],s=1)

plt.show()

# 最后显示画图结果
# plt.show()
