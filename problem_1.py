# -*- coding: utf-8 -*-

"""
本模块对应题目C中所研究的3个问题中的第1个
"""
from utils.coord_utils import transform_coord,delete_mistake_coord
from utils.other_utils import plot_track_to_html
import pandas as pd

def plot_track(file_path):
    """
    根据给定文件中的坐标点数据，画出行车路线图
    :param file_path:
    :return:
    """
    # 转换坐标
    after_transform_coord_file = transform_coord(file_path)

    # 删除错误坐标
    after_delete_coord_file = delete_mistake_coord(after_transform_coord_file)

    # 将坐标点数据嵌入到html文件中，直接通过浏览器打开html文件即可查看行车轨迹
    track_html_file = plot_track_to_html(after_delete_coord_file)

    # 返回行车路线图对应的html文件
    return track_html_file


def get_mileage_sum(file_path):
    """
    计算给定文件中的行车路线的行车里程
    :param file_path:数据文件
    :return:
    """
    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv(file_path, parse_dates=['location_time'], date_parser=dateparse)
    mileage_sum = df.iloc[-1]['mileage'] - df.iloc[0]['mileage']
    print('文件' + file_path + '中的行车路线的总行车里程为' + str(mileage_sum) + 'km')
    return mileage_sum


def get_avg_speed(file_path):
    """
    计算给定文件中的行车路线的平均行车速度
    :param file_path:
    :return:
    """
    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv(file_path, parse_dates=['location_time'], date_parser=dateparse)
    time_sum = 0.0
    for i in range(df.shape[0] - 1):
        p1 = df.iloc[i]
        p2 = df.iloc[i + 1]
        time_tmp = p2['location_time'].timestamp() - p1['location_time'].timestamp()
        # 5:63.948772678762005km/h  ,2:65.45772339960672km/h    ,   3:63.95787376360919km/h ,   4:63.948772678762005km/h
        interval = 4
        if (p1['gps_speed'] != 0 or p2['gps_speed'] != 0) and ( time_tmp < interval):
            time_sum = time_sum + time_tmp
    avg_speed = (df.iloc[-1]['mileage'] - df.iloc[0]['mileage']) / (time_sum / 3600)
    print('文件' + file_path + '中的行车路线的平均行车速度为：' + str(avg_speed) + 'km/h')
    return avg_speed



# plot_track('source_datas/AA00002.csv')
# get_mileage_sum('source_datas/AA00002.csv')
get_avg_speed('source_datas/AA00002.csv')