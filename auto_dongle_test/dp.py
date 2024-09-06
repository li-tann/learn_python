def print_dp_txt(filepath, idx, length):
    '''
    生成filepath文件, 打印length的数字, 其中第idx列是1, 其余都是0
    '''
    with open(filepath, 'w') as f:
        for i in range(length):
            if not i == idx:
                f.write('0')
            else:
                f.write('1')


def print_config_txt(filepath, id):
    '''
    写配置文件
    '''
    with open(filepath, 'w') as f:
        f.write('{0}\nID {0} \npar <   >\n'.format(id))

if __name__ == '__main__':
    print_dp_txt("dongle_permission.txt",2,218)