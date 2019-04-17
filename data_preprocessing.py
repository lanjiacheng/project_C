# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 加载数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
data_df = pd.read_csv('./source_datas/AA00004.csv', parse_dates=['location_time'], date_parser=dateparse)

print(data_df.shape)
data_df.dropna(inplace=True)
print(data_df.shape)