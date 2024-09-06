import os
import glob

'''
该脚本仅支持'标准文件结构'
root--dir1--*.tif
          --*.xml
    --dir2--*.tif
          --*.xml
    --dir3
    ......
'''

'''rootpath: 存放insar文件的根目录'''
rootpath="D:/1_Data/L-SAR_TEST/dinsar_mono_cut"
'''insar_console.exe的实际地址'''
console_path="D:/LandApp_make_installation_package/LandSAR_v1.3.1_beta/InSAR_Console.exe"


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
        ref_dem=glob.glob(dir+"/*RectSeg.tif")
        if(len(ref_dem)<1):
            with open(log_path,'a') as f:
                f.write("cannot find *RectSeg.tif\n")
            continue
        with open(log_path,'a') as f:
            f.write("ref_dem:{}\n".format(ref_dem[0]))
        
        target_dem=glob.glob(dir+"/*int_DEM.tif")
        if(len(target_dem)<1):
            with open(log_path,'a') as f:
                f.write("cannot find *int_DEM.tif\n")
            continue
        with open(log_path,'a') as f:
            f.write("target_dem:{}\n".format(target_dem[0]))
        

        dem_error_map = dir + "/dem_error_map.tif"

        # 生成config
        config="""DEM高程误差图计算
处理编号 180064
TARGET_DEM    <{}>
REF_DEM    <{}>
TAR_COH     <>
COH  0.6
HEI_THRES  20
OUTPUT_MAP   <{}>
            """.format(target_dem[0], ref_dem[0], dem_error_map)
        
        config_path=dir + "/config_180064.txt"
        with open(config_path,'w') as f:
            f.write(config)

        # 调用insar_console
        config_log = dir + "/CONFIG_180064.log"
        os.system("{} {}>>{}".format(console_path, config_path, config_log))
            

 