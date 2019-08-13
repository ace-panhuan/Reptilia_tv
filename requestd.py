import requests
import threading


# 父类，接受数据！传给子类
class RequestDelegate:
    def receive_data(self,data):
        pass


# 数据下载类
class Reqtest(threading.Thread):
    def __init__(self,delegate:RequestDelegate):
        super().__init__()
        self.__delegate = delegate    # 接受数据
        self.__url = None

    def request(self,url):
        self.__url = url
        self.start()

    def run(self):
        ret = requests.get(self.__url)
        #  得到数据data
        data = ret.content.decode("utf-8")
        # 数据转 码
        self.__delegate.receive_data(data)
        # 回传数据