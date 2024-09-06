from config import *
from dp import *
import os
import shutil

dict_len = len(id_dict)
for id in id_dict:
    idx = id_dict[id]

    id_dir = test_root+"/"+id
    if not os.path.exists(id_dir):
        os.mkdir(id_dir)

    dp_filepath = id_dir + "/dongle_permission.txt"
    print_dp_txt(dp_filepath, idx, dict_len)

    config_filepath = id_dir + "/config_{}.txt".format(id)
    print_config_txt(config_filepath, id)

    shutil.copy(dp_filepath, landsar_root + "/dongle_permission.txt")

    # result_txt = id_dir + "/result.txt"
    # os_result = os.system(insar_console + " " + config_filepath)
    # with open(result_txt) as f:
    #     f.write(os_result)