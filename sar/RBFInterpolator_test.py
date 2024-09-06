import numpy as np
from scipy.interpolate import RBFInterpolator
import osgeo.gdal as gdal

gdal.UseExceptions()

'''
scipy.interpolate.RBFInterpolator
曲面拟合算法
'''

demapth = 'D:/1_Data/DEM/AW3D/ALPSMLC30_N032E107_DSM.tif'
ds:gdal.Dataset=gdal.Open(demapth,gdal.GA_ReadOnly)
size = 1000
rb=ds.GetRasterBand(1)
data: np.ndarray = ds.ReadAsArray(0, 0, size, size)
data=data.astype(np.float32)
points = []
points_all = []
values = []
data_backup = np.zeros_like(data)
for i in range(0,size):
    for j in range(0,size):
        points_all.append([i,j])
        if 30 < i < 70 and 30 < j < 70:
            if i % 5 == 0 and j % 5 == 0:
                pass
            else:
                data_backup[i,j] = np.nan
                continue
        points.append([i,j])
        values.append(data[i,j])
        data_backup[i,j] = data[i,j]

# print(points)

# print(values)


# # 原始数据点的坐标
# points = np.array([[1, 1], [2, 2], [3, 5], [4, 9]])

# # 原始数据点的值
# values = np.array([1, 12, 3, 4])

# 创建RBF插值器实例
rbf = RBFInterpolator(points, values, 50,  kernel='cubic')

# # 需要插值的点的坐标
# x_to_interpolate = np.linspace(1, 4, 10)[:, None]  # 生成10个点在1到4之间

# 进行插值
interpolated_values = rbf(points_all)

dst = np.zeros_like(data)
for i in range(0,size):
    for j in range(0,size):
        dst[i,j] = interpolated_values[i * size + j]

driver = gdal.GetDriverByName("GTiff")
ds = driver.Create("D:/1_Data/DEM/AW3D/ALPSMLC30_N032E107_DSM_interped.tif", size, size, 1, gdal.GDT_Float32)
rb = ds.GetRasterBand(1)
rb.WriteArray(dst)

ds2 = driver.Create("D:/1_Data/DEM/AW3D/ALPSMLC30_N032E107_DSM_origin.tif", size, size, 1, gdal.GDT_Float32)
rb2 = ds2.GetRasterBand(1)
rb2.WriteArray(data)

ds3 = driver.Create("D:/1_Data/DEM/AW3D/ALPSMLC30_N032E107_DSM_rm_point.tif", size, size, 1, gdal.GDT_Float32)
rb3 = ds3.GetRasterBand(1)
rb3.WriteArray(data_backup)

# # 打印插值结果
# print(interpolated_values)