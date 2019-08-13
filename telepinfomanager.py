import requestd
import re
from teleplay import Teleplay

# 下载并解析存储
#电视剧信息类


class TeleplayManager(requestd.RequestDelegate):
    def __init__(self):
        self.__request = requestd.Reqtest(self)

     #  下载数据
    def download(self,url):
        self.__request.request(url)

    # 重写方法接受数据
    def receive_data(self,data):
        self.analyze_data(data)

    #解析html文件
    def analyze_data(self,data):
        info = Teleplay()
        # 获取电视剧名字
        pattern = '"name":(.*)"director":'
        ret = re.search(pattern,data,re.S)
        pattern = '"(.*)",.*"url"'
        rets = re.search(pattern,ret.group(1),re.S)
        info.set_name(rets.group(1))

        # 获取导演名
        pattern = '"@type":(.*)"author":'
        ret = re.search(pattern,data,re.S)
        ls = ret.group(1).split('"')
        info.add_director(ls[9])

        # 获取演员名
        pattern = '"actor":(.*)"datePublished"'
        ret = re.search(pattern,data,re.S)
        ls = ret.group(1).split("}")

        for i in ls[:-1]:
            pattern = '"name":(.*)'
            ret = re.search(pattern,i,re.S)
            info.add_author(ret.group(1))
        # 获取简介
        pattern = '"description":(.*)"@type": "TVSeries"'
        ret = re.search(pattern,data,re.S)
        info.add_synopsis(ret.group(1))

        # 获取评分
        pattern = '"ratingValue": "(.*)"'
        ret = re.search(pattern,data)
        info.set_score(ret.group(1))
        wo = str(info)
        paths = r"D:\3.txt"
        file = open(paths,'a',encoding="utf-8")
        file.write(wo)
        print(wo)




path = "https://movie.douban.com/subject/26787123/"
xia = TeleplayManager()
xia.download(path)
