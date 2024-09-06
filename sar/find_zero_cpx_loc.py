import osgeo.gdal as gdal
import sys

tif_path = r'D:\1_Data\L-SAR_TEST\dinsar_mono_cut\LT1AA_0000084983_0000087783_E113.0_N40.0_20230321_20230329\20230321_Cut_20230329_Cut_int.tif'

try:
    ds: gdal.Dataset=gdal.Open(tif_path)
except RuntimeError as e:
    print( 'Unable to open %s'% tif_path)
    sys.exit(1)

tar_cols = ds.RasterXSize #图像长度
tar_rows = ds.RasterYSize #图像宽度

rb: gdal.Band= ds.GetRasterBand(1)
datatype = rb.DataType

if datatype != gdal.GDT_CFloat32:
    print('datatype != gdal.GDT_CFloat32')

print(gdal.GetDataTypeName(datatype))

