# -*- coding: utf-8 -*-


"""
将源数据中的wgs84标准的经纬度坐标转换成百度地图所用bd09标准的经纬度坐标，
然后再讲转换后的数据保存到./middle_data/coord_transformed_data/目录下，文件名不变。
"""


import pandas as pd
from utils.coord_utils import wgs84_to_bd09


# 设置源文件路径
src_dir = './source_data/'
src_file = 'AA00002.csv'
src_path = src_dir + src_file

# 加载数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
data_df = pd.read_csv(src_path, parse_dates=['location_time'], date_parser=dateparse)

# 转换经纬度坐标
coords = data_df.apply(lambda vs:wgs84_to_bd09(vs['lng'],vs['lat']),axis=1)

# 将原来的经纬度坐标替换成新的经纬度坐标
lngs = []
lats = []
for coord in coords:
    lngs.append(coord[0])
    lats.append(coord[1])
data_df['lng'] = pd.Series(lngs)
data_df['lat'] = pd.Series(lats)

# 存储转换过经纬度坐标的数据
new_path = './middle_data/coord_transformed_data/'+src_file
data_df.to_csv(new_path)

print('转换' + src_path + '经纬度坐标(wgs84 to bd09)完成！\n已将转换后的数据保存到' + new_path + '中！')