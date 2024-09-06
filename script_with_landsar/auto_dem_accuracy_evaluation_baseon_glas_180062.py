import os
import glob

from xml.dom.minidom import parse
import xml.dom.minidom


'''
该脚本仅支持'标准文件结构'
root--dir1--*.tif
          --*.xml
    --dir2--*.tif
          --*.xml
    --dir3
    ......
'''


rootpath="D:/1_Data/L-SAR_TEST/dinsar_mono_cut"
'''rootpath: 存放insar文件的根目录'''

glasrootpath="F:/public/guihua/share/InSAR/GLAS"
'''glasrootpath: 存放GLAS点的根目录'''

console_path="D:/LandApp_make_installation_package/LandSAR_v1.3.1_beta/InSAR_Console.exe"
'''console_path: insar_console.exe的实际地址'''

for filepath,dirnames,filenames in os.walk(rootpath):
    # print(len(dirnames),",",dirnames)
    for dirname in dirnames:
        if len(dirname) < 1:
            pass

        dir=rootpath+"/"+dirname
        '''log_path: '''
        log_path=dir + "/EVA_DEM.log"
        if os.path.exists(log_path):
            os.remove(log_path)

        # 查找RectSeg.tif 和 _DEM.tif 
        int_xml=glob.glob(dir+"/*int.xml")
        if(len(int_xml)<1):
            with open(log_path,'a') as f:
                f.write("cannot find *int.xml\n")
            continue
        with open(log_path,'a') as f:
            f.write("int_xml:{}\n".format(int_xml[0]))
        
        target_dem=glob.glob(dir+"/*int_DEM.tif")
        if(len(target_dem)<1):
            with open(log_path,'a') as f:
                f.write("cannot find *int_DEM.tif\n")
            continue
        with open(log_path,'a') as f:
            f.write("target_dem:{}\n".format(target_dem[0]))
        

        glas_screen_filepath= dir + "/glas_screen.txt"
        glas_dem_error_filepath = dir + "/glas_dem_error.txt"

        # 生成config
        config="""GLAS点筛选与DEM精度评价
处理编号 180062
GLAS数据类型_0glas文件_1glas目录   1
GLAS文件路径或二级搜索目录    <{}>
int_XML   <{}>
REF_DEM    <>
TAR_DEM     <{}>
TAR_COH    <>
COH  0.6
GLAS_RANGE    70
HEI_DIFF_THRES   50
VALID_DEM_PERCENTAGE_THRES  0.7
GLAS_RANGE_NORTH   0
GLAS_RANGE_SOUTH   0
GLAS_RANGE_WEST   0
GLAS_RANGE_EAST   0
GLAS_GCP_PATH  <>
GLAS_SCREEN_PATH <{}>
DEM_ERROR_PATH   <{}>
            """.format(glasrootpath, int_xml[0], target_dem[0], glas_screen_filepath, glas_dem_error_filepath)
        
        config_path=dir + "/config_180062.txt"
        with open(config_path,'w') as f:
            f.write(config)

        # 调用insar_console
        config_log = dir + "/CONFIG_180062.log"
        os.system("{} {}>>{}".format(console_path, config_path, config_log))
            

 