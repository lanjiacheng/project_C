# -*- coding: utf-8 -*-


import pandas as pd
from matplotlib import pyplot as plt


def get_accelerations(file_path):
    """
    计算file_path文件中的行车路线的每两点之间的加速度
    :param file_path:
    :return:
    """
    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv(file_path, parse_dates=['location_time'], date_parser=dateparse)
    accelerations = []
    for i in range(df.shape[0] - 1):
        p1 = df.iloc[i]
        p2 = df.iloc[i + 1]
        time_tmp = p2['location_time'].timestamp() - p1['location_time'].timestamp()
        interval = 5
        if (p1['gps_speed'] != 0 and p2['gps_speed'] != 0) and (time_tmp < interval):
            acceleration = (p2['gps_speed'] - p1['gps_speed']) / float(time_tmp)  # 求两点间的加速度
            accelerations.append(acceleration)
        print(i)
    return accelerations


def get_all_accelerations(dir_path):
    """
    计算给定文件夹中的所有文件的行车路线的所有加速度
    :param dir_path:
    :return:
    """


accelerationscs = get_accelerations('source_datas/AA00002.csv')
plt.scatter(range(len(accelerationscs)), accelerationscs,s=0.1)
plt.show()
