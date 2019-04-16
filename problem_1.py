"""
本模块对应题目C中所研究的3个问题中的第1个
"""
from utils.coord_utils import transform_coord,delete_mistake_coord
from utils.other_utils import plot_track_to_html

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
    plot_track_to_html(after_delete_coord_file)


plot_track('source_data/AA00004.csv')

# plot_track_to_html('middle_data/coord_transformed_data/AB00006.csv')