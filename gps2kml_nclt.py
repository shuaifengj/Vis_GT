"""
读取NCLT数据集的gps数据，生成kml文件
"""
import pandas as pd
from lxml import etree
import numpy as np


# 定义弧度到度数的转换函数
def radians_to_degrees(radians):
    return radians * 180 / np.pi

# 读取CSV文件
df = pd.read_csv('/mnt/data/nclt/data/sensor_data/2012-01-08_sen/gps_rtk.csv')

# 每5个抽取一个点
# sampled_df = df.iloc[::2]
sampled_df = df
# 创建KML文件的根元素
kml = etree.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
document = etree.SubElement(kml, 'Document')

# 创建LineString元素，用于存储轨迹点
placemark = etree.SubElement(document, 'Placemark')
line_string = etree.SubElement(placemark, 'LineString')
coordinates = etree.SubElement(line_string, 'coordinates')

# 遍历抽取的数据并生成坐标字符串
coords = ""
for index, row in sampled_df.iterrows():
    # 将需要转换的列进行度数到弧度的转换
    row[3] = radians_to_degrees(row[3])
    row[4] = radians_to_degrees(row[4])
    coords += f"{row[4]},{row[3]},0 "  # 经度、纬度、高度（这里假设高度为0）
coordinates.text = coords.strip()

# 将KML对象转换为字符串
kml_str = etree.tostring(kml, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# 保存KML文件
output_filename = 'gps.kml'
with open(output_filename, 'wb') as file:
    file.write(kml_str)

print(f"KML文件已保存为 {output_filename}")
