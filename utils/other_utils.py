# -*- coding: utf-8 -*-


import json
import pandas as pd

def get_points_json_from_dataFram(df):
    """
    将pandas的dataFram数据转换成json格式字符串
    """
    points = df.apply(lambda vs: {
        "lat": vs['lat'],
        "lng": vs['lng']
    }, axis=1)
    points_list = points.tolist()
    points_json = json.dumps(points_list)
    return points_json

def plot_track_to_html(file_path):
    """
    将转换过经纬度坐标的csv文件的数据转换成json各式数据，然后嵌入到html的js脚本中，用浏览器打开html文件即可看到路线图
    :param file_path:
    :return:
    """
    file_name = file_path[-11:]

    # 加载数据
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    data_df = pd.read_csv(file_path, parse_dates=['location_time'], date_parser=dateparse)

    points_json = get_points_json_from_dataFram(data_df)

    model_html = open('plot_track_model.html', 'r', encoding='utf-8').read()
    html = model_html.replace('points_json_str_tmp', points_json)

    new_path = './plot_track_htmls/' + file_name[:-4] + '.html'
    open(new_path, 'w', encoding='utf-8').write(html)

    print('已将' + file_path + '文件的位置点经纬度嵌入' + new_path + '并绘制成行车轨迹，直接用浏览器打开即可查看！')

    return new_path