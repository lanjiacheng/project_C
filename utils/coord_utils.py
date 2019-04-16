# -*- coding: utf-8 -*-
import math
from math import sin, asin, cos, radians, fabs, sqrt
import pandas as pd

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方


def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    """
    根据两点的经纬度计算两点的距离
    :param lat0:
    :param lng0:
    :param lat1:
    :param lng1:
    :return:
    """

    EARTH_RADIUS = 6371  # 地球平均半径，6371km

    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance


def transform_coord(file_path):
    """
    将文件中的坐标点的经纬度进行转换，转成百度地图标准的经纬度坐标，然后将转换后的坐标数据保存到./middle_data/coord_transformed_data/目录下的同名文件
    :param file_path:
    :return:
    """
    print('开始对文件' + file_path + '中的坐标进行转换！')

    file_name = file_path[-11:]

    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    data_df = pd.read_csv(file_path, parse_dates=['location_time'], date_parser=dateparse)

    # 转换经纬度坐标
    coords = data_df.apply(lambda vs: wgs84_to_bd09(vs['lng'], vs['lat']), axis=1)

    # 将原来的经纬度坐标替换成新的经纬度坐标
    lngs = []
    lats = []
    for coord in coords:
        lngs.append(coord[0])
        lats.append(coord[1])
    data_df['lng'] = pd.Series(lngs)
    data_df['lat'] = pd.Series(lats)

    # 存储转换过经纬度坐标的数据
    new_path = './middle_data/coord_transformed_data/' + file_name
    data_df.to_csv(new_path)
    print('转换' + file_path + '经纬度坐标(wgs84 to bd09)完成！\n已将转换后的数据保存到' + new_path + '中！')
    return new_path


def delete_mistake_coord(file_path):
    """
    删除文件中错误坐标点，然后将剩余坐标点保存到./middle_data/after_choose_datas/目录下同名文件
    :param file_path:
    :return:
    """

    print('开始删除文件' + file_path + '中的错误坐标！')

    file_name = file_path[-11:]

    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv(file_path, parse_dates=['location_time'],
                     date_parser=dateparse)

    # 通过经纬度计算两个点之间的距离
    def get_distance_of_scope_points(scope_points):
        distances = []
        for i in range(scope_points.shape[0] - 1):
            lng1 = scope_points.iloc[i]['lng']
            lat1 = scope_points.iloc[i]['lat']
            lng2 = scope_points.iloc[i + 1]['lng']
            lat2 = scope_points.iloc[i + 1]['lat']
            distance = get_distance_hav(lat1, lng1, lat2, lng2)
            distances.append(distance)
        return sum(distances)

    indexs_to_choose = []
    # 2  0.03
    scope = 2
    max_scope_distance = 0.03 * (scope - 1)  # 0.01420716022983939

    len = df.shape[0] - scope

    for i in range(len):
        scope_points = df.iloc[i:i + scope]
        current_scope_distance = get_distance_of_scope_points(scope_points)
        if current_scope_distance < max_scope_distance:
        # if df.iloc[i]['gps_speed'] > 0:
            indexs_to_choose.append(i)
        print('在delete_mistake_coord(删除错误坐标)方法中处理数据进度达到：\t' + str(float(i)/len*100)[:4] + '%')

    df_after_choose = df.iloc[indexs_to_choose]
    new_path = './middle_data/after_choose_datas/' + file_name
    df_after_choose.to_csv(new_path)
    print('已经删除' + file_path + '文件中的错误坐标点，并将剩下的数据保存到' + new_path)
    return new_path