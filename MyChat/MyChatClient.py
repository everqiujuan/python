import socket
import re
import threading

class ChatClient(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.username = name
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_addr = ('10.20.151.140', 8878)
        # 在线
        self.online = False

    def run(self):
        while self.online:
            self.__recv_message()


    def begin(self):
        if not self.__login():
            return
        self.online = True

        self.start()    # 子线程接收数据
        while True:
            s = input("\n***操作说明***\n选择你的操作:\n1.显示在线用户列表\n0.下线退出\n输入\">>在线用户名:内容\"和在线用户聊天\n")
            if s == "1":
                self.__show_list()
            elif s == "0":
                self.__logout()
                self.online = False
                break
            else:
                # 尝试发送信息
                if not self.__send_message(s):
                    print("输入错误，重试!")

    # 发送聊天数据
    def __send_message(self, s:str):
        # to在线用户名: 内容
        ret = re.search("^>>(.*):(.*)$", s)
        if not ret or "|" in s:
            return False
        otherusername = ret.group(1)
        message = ret.group(2)
        self.client_socket.sendto("SENDTO|{}|{}|{}".format(otherusername,
                                                           self.username,
                                                           message).encode("utf-8"), self.server_addr)
        return True

    def __login(self):
        # 上线，立即发送登陆口令
        self.client_socket.sendto("LOGIN|{}".format(self.username).encode("utf-8"), self.server_addr)
        # 回值，表示登陆是否成功
        data, addr = self.client_socket.recvfrom(1024)
        print(data.decode("utf-8"))
        if data.decode("utf-8").startswith("登陆成功"):
            return True
        else:
            return False

    # 显示在线列表
    def __show_list(self):
        self.client_socket.sendto("LIST|".encode("utf-8"), self.server_addr)


    # 下线
    def __logout(self):
        self.client_socket.sendto("LOGOUT|{}".format(self.username).encode("utf-8"), self.server_addr)
        # data, addr = self.client_socket.recvfrom(1024)
        # print(data.decode("utf-8"))
        return True


    # 客户端单独写一个函数接收发来的聊天信息
    def __recv_message(self):
        data, addr = self.client_socket.recvfrom(2048)
        print(data.decode("utf-8"))




client = ChatClient("老潘")
client.begin()
