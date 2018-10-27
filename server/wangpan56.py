from download_html import HtmlDownloader as html_downloader
from html_analyze import HtmlParser as html_parser
from url_controller import UrlControl as url_control

import urllib.parse


class wangpan56:
    def __init__(self):

        self.download_html = html_downloader()  # 下载器
        self.html_analyze = html_parser()  # 解析器
        self.url_control_dil = url_control()  # 存储详情页
        pass

    def start(self, keywords, index=1):
        key="+".join(keywords)
        url="http://www.56wangpan.com/search/o1kw{}pg{}".format(urllib.parse.quote(key), index)
        print(url)
        html_content = self.download_html.download_html(url)
        # print(html_content)
        if not html_content:
            return False
        xpath={
            'url':{
                'xpath': '//div[@class="info clear"]/div[@class="address"]/text()',
            },
            'title':{
                'xpath': '//div[@class="info clear"]/div[@class="title"]/a/@title'
            },
            'binary': True,
            'ChineseGarbled': True,
            'reorganization': ['title', 'url'],
        }
        analyze_result = self.html_analyze.paser_xpath(html_content, xpath)
        # print(analyze_result)

        return analyze_result




if __name__ == '__main__':
    a=wangpan56()
    a.start(["你好", "疯子"], 1)

