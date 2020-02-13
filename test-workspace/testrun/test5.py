from urllib import request
import re
from bs4 import BeautifulSoup

class Spider():
    url='https://www.panda.tv/all?pdt=1.18.pheader-n.1.7hk3ljl6qha'
    root_pattern = '<div class="video-info">([\S\s]*?)</div>'
    name_pattern = 'title="([\s\S]*?)">\n'
    num_pattern = '</i>(.*)</span>'
    def __fetch_content(self):
        # r=request.urlopen(Spider.url)
        # rs=r.read()
        # rs=str(rs,encoding='utf-8')
        rs = request.urlopen(Spider.url).read().decode('utf-8')
        # print(type(rs))

        return rs

    def __analyze(self,htmls):
        h1=re.findall(Spider.root_pattern,htmls)
        for i in h1:
            #用Soup方法获取想要的 姓名 和 点击数
            soup = BeautifulSoup(i.encode('utf-8'))
            results_name = soup.find_all('span',class_='video-nickname')
            results_num = soup.find_all('span',class_='video-number')
            #findall方法操作string类型所以要先将list转类型
            results_name = str(results_name)
            results_num = str(results_num)

            name = re.findall(Spider.name_pattern,results_name)
            #姓名字段去空格
            New_list = []
            for i in name:
                New_list.append(i.replace(" ", "").replace("\n",""))
                name = New_list

            num = re.findall(Spider.num_pattern, results_num)

            self.__author(name,num)


    # 用lambda函数将两个list放入字典
    def __author(self,name,num):
        final_dict = dict(map(lambda x, y: [x, y], name, num))
        print(final_dict)
        self.sort_by_value(final_dict)

    def sort_by_value(self,final_dict):
        pass

    def go(self):
        htmls = self.__fetch_content()
        self.__analyze(htmls)



spider=Spider()
spider.go()