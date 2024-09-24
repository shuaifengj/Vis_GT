"""
Iterate through each frame of oxts data and generate a GPS file
"""
import os
def read_gps_data(oxts_folder):
    gps_data = []
    for filename in sorted(os.listdir(oxts_folder)):
        if filename.endswith('.txt'):
            with open(os.path.join(oxts_folder, filename), 'r') as file:
                line = file.readline()
                data = line.split()
                gps_data.append({
                    'frame': int(filename.split('.')[0]),  # 假设文件名为帧编号
                    'lat': float(data[0]),
                    'lon': float(data[1]),
                    'alt': float(data[2]),
                    'roll': float(data[3]),
                    'pitch': float(data[4]),
                    'yaw': float(data[5]),
                })
    return gps_data

def write_gps_to_file(gps_data, output_file):
    with open(output_file, 'w') as file:
        file.write("frame,lat,lon\n")  # 文件头
        for data in gps_data:
            file.write(f"{data['frame']},{data['lat']},{data['lon']}\n")

# 读取指定文件夹中的GPS数据
oxts_folder = '/home/shorwin/Downloads/2011_10_03_drive_0027_sync/2011_10_03/2011_10_03_drive_0027_sync/oxts/data'
gps_data = read_gps_data(oxts_folder)

# 输出文件路径
output_file = '/home/shorwin/Downloads/2011_10_03_drive_0027_sync/2011_10_03/2011_10_03_drive_0027_sync/oxts/data/gps_data.csv'

# 将GPS数据写入文件
write_gps_to_file(gps_data, output_file)

print(f"GPS数据已写入文件 {output_file}")
