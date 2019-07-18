import socket

# 管理用户的账户信息
class UserInfo:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

# 服务器主程序 管理用户信息，转发聊天数据
class ChatSever:
    def __init__(self):
        # 字典记录用户信息
        self.userInfos = {}
        # 服务器的socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('10.20.151.140', 8878))

    # 启动服务器
    def start(self):
        self.__run()

    def __run(self):
        # 不断收发转发数据
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            data = data.decode("utf-8")
            # 解析data
            self.__analzy_data(data, addr)

    # 解析数据
    def __analzy_data(self, data, addr):
        # 规定应用层协议类似http
        # 登陆:"Login|username"
        # 客户请求显示在线列表:"List|"
        # 发消息"SENDTO|otherusername|username|message"
        # 下线:"Logout|username"
        if data.startswith("LOGIN|"):
            self.__login(data[6:], addr)
            pass
        elif data.startswith("LIST|"):
            self.__sendUserList(addr)
            pass
        elif data.startswith("SENDTO|"):
            self.__send_message(data[7:], addr)
            pass
        elif data.startswith("LOGOUT|"):
            self.__logout(data[7:], addr)
            pass

    # 发送聊天到某人
    def __send_message(self, s:str, addr):
        # othername|username|message
        ls = s.split("|")
        othername = ls[0]
        username = ls[1]
        message = ls[2]
        # 找到对方地址
        try:
            x = self.userInfos[othername]
            # 发给other的数据
            s = "\n===收到消息===\nfrom:【{}】:{}\n".format(username, message)
            print(othername, x.addr)
            self.server_socket.sendto(s.encode("utf-8"), x.addr)
        except KeyError:
            pass


    @staticmethod
    def check_username(username):
        if len(username) < 1:
            return False
        if "\n" in username:
            return False
        if " " in username:
            return False
        if "|" in username:
            return False
        return True

    # 登陆
    def __login(self, username, addr):
        try:
            x = self.userInfos[username]
            # addr是客户地址，发送回执
            self.server_socket.sendto("登陆失败，用户名已存在!".encode("utf-8"), addr)
        except KeyError:
            # 没有这个用户
            # 登陆这个用户 创建用户，加入字典
            if not ChatSever.check_username(username):
                self.server_socket.sendto("登陆失败，用户名已存在!".encode("utf-8"), addr)
                return
            self.userInfos[username] = UserInfo(username, addr)
            self.server_socket.sendto("登陆成功!".encode("utf-8"), addr)
            print("%s登陆成功!" % username)

    # 下辖
    def __logout(self, username, addr):
        try:
            self.userInfos.pop(username)
            print("%s下线!" % username)
            self.server_socket.sendto("你已成功下线!".encode("utf-8"), addr)
        except KeyError:
            self.server_socket.sendto("你已下线失败!".encode("utf-8"), addr)

    # 显示在线列表
    def __sendUserList(self, addr):
        s = "\n===在线用户===\n"
        for username in self.userInfos.keys():
            s += "【" + username + "】\n"
        self.server_socket.sendto(s.encode("utf-8"), addr)


chat_server = ChatSever()
chat_server.start()