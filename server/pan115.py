from download_html import HtmlDownloader as html_downloader
from html_analyze import HtmlParser as html_parser
from url_controller import UrlControl as url_control

import urllib.parse
import time


class pan115:
    def __init__(self):

        self.download_html = html_downloader()  # 下载器
        self.html_analyze = html_parser()  # 解析器
        self.url_control_dil = url_control()  # 存储详情页

        self.result = []
        pass

    def start(self,keywords,index=1):
        key="+".join(keywords)
        url="http://www.guanggua.com/search?key={}&source=1&p={}".format(urllib.parse.quote(key), index)
        # print(url)
        try:
            html_content = self.download_html.download_html(url)
            # print(html_content)
            if not html_content:
                return False
            xpath={
                'url':{
                    'xpath': '//section[@class="result-list container"]//ul/li[1]/a/@href',
                    'base_url': 'http://www.guanggua.com/',
                },
                # 'binary': True,
            }
            analyze_result = self.html_analyze.paser_xpath(html_content, xpath)
            self.url_control_dil.add_new_urls(analyze_result['url'])
            # print(analyze_result)
        except:
            pass
        time.sleep(1)



        while self.url_control_dil.has_new_url():
            try:
                url = self.url_control_dil.get_new_url()
                # url='http://www.guanggua.com/file/A4SdYea2'
                html_content = self.download_html.download_html(url)
                # print(html_content)
                if not html_content:
                    return False
                xpath = {
                    'title': {
                        'xpath': '//div[@class="res-details"]//div[@class="header-title text-limit"]//text()'
                    },
                    'url': {
                        'xpath': '//div[@class="res-details"]/a/@href'
                    },
                    'reorganization': ['title','url'],
                    'binary': True,
                    'ChineseGarbled': True,
                }
                analyze_result = self.html_analyze.paser_xpath(html_content, xpath)
                # print(analyze_result)
                if isinstance(analyze_result, list):
                    self.result += analyze_result
                    print(analyze_result)
            except:
                pass
            # print(self.url_control_dil.has_new_url())
            time.sleep(1)

        print(self.result)
        return self.result


if __name__ == '__main__':
    a=pan115()
    a.start(["你好", "疯子"], 1)

