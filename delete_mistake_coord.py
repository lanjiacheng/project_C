# -*- coding: utf-8 -*-

import pandas as pd
from utils.coord_utils import *

# 加载数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv('middle_datas/coord_transformed_data/AA00002.csv', parse_dates=['location_time'], date_parser=dateparse)
df.dropna(axis=1,inplace=True)

# 通过经纬度计算两个点之间的距离
def get_distance_of_scope_points(scope_points):
    distances = []
    for i in range(scope_points.shape[0] - 1):
        lng1 = scope_points.iloc[i]['lng']
        lat1 = scope_points.iloc[i]['lat']
        lng2 = scope_points.iloc[i + 1]['lng']
        lat2 = scope_points.iloc[i + 1]['lat']
        distance = get_distance_hav(lat1,lng1,lat2,lng2)
        distances.append(distance)
    return sum(distances)


indexs_to_choose = []
scope = 5
max_scope_distance = 0.03 * (scope - 1)                   # 0.01420716022983939

for i in range(df.shape[0] - scope):
    scope_points = df.iloc[i:i + scope]
    current_scope_distance = get_distance_of_scope_points(scope_points)
    if current_scope_distance < max_scope_distance:
        indexs_to_choose.append(i)
    print(i)

df_after_choose = df.iloc[indexs_to_choose]
df_after_choose.to_csv('./middle_datas/after_choose_datas/AA00002.csv')