from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 创建一个授权器对象
authorizer = DummyAuthorizer()

# 添加一个用户
authorizer.add_user("user", "12345", "D:/2_Codes/python/ftp_server/root", perm="elradfmwM")

# 配置FTPHandler
handler = FTPHandler
handler.authorizer = authorizer

# 创建FTP服务器实例
server_address = ("192.168.110.129", 21)  # 服务器地址和端口
server = FTPServer(server_address, handler)

# 运行服务器
server.serve_forever()