import ftplib
import time

ftp = ftplib.FTP('192.168.110.129')  # 替换为你的FTP服务器地址
ftp.encoding ='gbk'
ftp.connect('192.168.110.129', 21)


ftp.login('user', '12345')

i=0
childfile_last=ftp.nlst()
childfile_size:int = len(childfile_last)
print("init childfile size: ", childfile_size )


# print("childfile[1].size:", ftp.size('123.png')/1e6, 'Mb')
while(i<50):
    i=i+1
    time.sleep(0.2)
    ftp.dir()
    continue
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    # print(ftp.dir())
    childfile = ftp.nlst()
    # print(childfile)
    for cld in childfile:
        print(cld, ":",ftp.voidcmd("MDTM "+ cld ))

    # print("childfile[1].size:", ftp.size(childfile[0])/1e6, 'Mb')
    # if len(childfile) != childfile_size:
    #     print("childfile[1].size:", ftp.size(childfile[1])/1e6, 'Mb')
    

print("ftp.close")

ftp.close()