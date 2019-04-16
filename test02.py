# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd


def f1():
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv('source_data/AA00004.csv', parse_dates=['location_time'], date_parser=dateparse)
    plt.subplot(3, 1, 1)
    plt.xlim(xmin=df['location_time'][0], xmax=df['location_time'][df.shape[0] - 1])
    plt.scatter(df['location_time'], df['mileage'], s=0.1, edgecolors='red')
    plt.xlabel('时间')
    plt.ylabel('里程数')

    plt.subplot(3, 1, 2)
    plt.xlim(xmin=df['location_time'][0], xmax=df['location_time'][df.shape[0] - 1])
    plt.scatter(df['location_time'], df['lng'], s=0.1, edgecolors='red')
    plt.xlabel('时间')
    plt.ylabel('经度')

    plt.subplot(3, 1, 3)
    plt.xlim(xmin=df['location_time'][0], xmax=df['location_time'][df.shape[0] - 1])
    plt.scatter(df['location_time'], df['lat'], s=0.1, edgecolors='red')
    plt.xlabel('时间')
    plt.ylabel('维度')
    plt.show()


def f2():
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv('source_data/AA00004.csv', parse_dates=['location_time'], date_parser=dateparse)
    distances = []
    for i in range(df.shape[0] - 1):
        distance = df.iloc[i + 1]['mileage'] - df.iloc[i]['mileage']
        distances.append(distance)
    plt.scatter(range(len(distances)), distances, s=0.1, edgecolors='red')
    plt.show()


def f3():
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv('source_data/AA00004.csv', parse_dates=['location_time'], date_parser=dateparse)
    df = df.iloc[:5000]

    index_pairs = []

    for i in range(df.shape[0] - 1):
        df1 = df.iloc[i]
        df2 = df.iloc[i + 1]
        if df2['location_time'].timestamp() - df1['location_time'].timestamp() > 10:
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
    plt.xlim(xmin=df['location_time'][0], xmax=df['location_time'][df.shape[0] - 1])
    for split_df in split_dfs:
        plt.scatter(split_df['location_time'], split_df['gps_speed'],s=1)

    plt.show()


# f2()
f3()