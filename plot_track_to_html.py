# -*- coding: utf-8 -*-


"""
将转换过经纬度坐标的csv文件的数据转换成json各式数据，然后嵌入到html的js脚本中，用浏览器打开html文件即可看到路线图
"""

import pandas as pd
from utils.other_utils import get_points_json_from_dataFram


# 设置源文件路径
src_dir = './middle_data/after_choose_datas/'
src_file = 'AA00002.csv'
src_path = src_dir + src_file

# 加载数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
data_df = pd.read_csv(src_path, parse_dates=['location_time'], date_parser=dateparse)

points_json = get_points_json_from_dataFram(data_df)

model_html = open('plot_track_model.html','r',encoding='utf-8').read()
html = model_html.replace('points_json_str_tmp',points_json)

new_path = './plot_track_htmls/'+src_file[:-4]+'.html'
open(new_path,'w',encoding='utf-8').write(html)

print('已将' + src_path + '文件的位置点经纬度嵌入' + new_path + ',直接用浏览器打开即可查看！')