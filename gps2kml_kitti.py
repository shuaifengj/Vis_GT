"""
读取KITTI数据集的gps数据,生成kml文件
"""
import pandas as pd
from lxml import etree
import numpy as np


# 定义弧度到度数的转换函数
def radians_to_degrees(radians):
    return radians * 180 / np.pi

# 读取CSV文件
df = pd.read_csv('./source_files/gps_data.csv')

# 每5个抽取一个点
# sampled_df = df.iloc[::2]
sampled_df = df
# 创建KML文件的根元素
kml = etree.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
document = etree.SubElement(kml, 'Document')


# 添加KML文件的名称
name = etree.SubElement(document, 'name')
name.text = "GPS KITTI"

# 定义样式
style = etree.SubElement(document, 'Style', id="yellowLineGreenPoly")
line_style = etree.SubElement(style, 'LineStyle')
color = etree.SubElement(line_style, 'color')
color.text = "ff0000ff"  # 线条颜色，ARGB格式
width = etree.SubElement(line_style, 'width')
width.text = "10"  # 线条宽度

# 创建LineString元素，用于存储轨迹点
placemark = etree.SubElement(document, 'Placemark')
placemark_name = etree.SubElement(placemark, 'name')
placemark_name.text = "Track"
style_url = etree.SubElement(placemark, 'styleUrl')
style_url.text = "#yellowLineGreenPoly"


line_string = etree.SubElement(placemark, 'LineString')
coordinates = etree.SubElement(line_string, 'coordinates')

# 遍历抽取的数据并生成坐标字符串
coords = ""
for index, row in sampled_df.iterrows():
    coords += f"{row[2]},{row[1]},0 "  # 经度、纬度、高度（这里假设高度为0）
coordinates.text = coords.strip()

# 将KML对象转换为字符串
kml_str = etree.tostring(kml, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# 保存KML文件
output_filename = 'gps_kitti.kml'
with open(output_filename, 'wb') as file:
    file.write(kml_str)

print(f"KML文件已保存为 {output_filename}")
