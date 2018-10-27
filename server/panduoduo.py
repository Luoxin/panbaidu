from download_html import HtmlDownloader as html_downloader
from html_analyze import HtmlParser as html_parser
from url_controller import UrlControl as url_control

import urllib.parse
import time


class panduoduo:
    def __init__(self):

        self.download_html = html_downloader()  # 下载器
        self.html_analyze = html_parser()  # 解析器
        self.url_control_dil = url_control()  # 存储详情页

        self.result = []
        pass

    def start(self,keywords,index=1):
        try:  # 列表页
            key = " ".join(keywords)
            url='http://www.panduoduo.net/s/comb/n-{}&ty-bd/{}'.format(urllib.parse.quote(key), index)
            # print(url)
            # return 0
            html_content = self.download_html.download_html(url)
            # print(html_content)
            if not html_content:
                return False
            xpath = {
                "url": {
                    'xpath': '//h3/a/@href',
                    'base_url': 'http://www.panduoduo.net/'
                },
                # 'title':{
                #     'xpath': '//h3/a/@title',
                #     'unicode': True,
                # },
                'binary': True,
                'gzip': True,
                'reorganization': ['title', 'url'],
            }
            analyze_result = self.html_analyze.paser_xpath(html_content,xpath)
            if analyze_result is None:
                xpath['gzip'] = False
                analyze_result = self.html_analyze.paser_xpath(html_content, xpath)

            # print(analyze_result)
            self.url_control_dil.add_new_urls(analyze_result["url"])
        except:
            pass

        time.sleep(1)

        while self.url_control_dil.has_new_url():
            try:  # 详情页
                url=self.url_control_dil.get_new_url()
                # url='http://www.panduoduo.net/r/44174413'
                html_content = self.download_html.download_html(url)
                # print(html_content)
                if not html_content:
                    return False
                xpath={
                    'title': {
                        'xpath': '//h1/text()'
                    },
                    'url':{
                        'xpath': '//a[@class="dbutton2"]/@href'
                    },
                    'reorganization': ['title', 'url'],
                }
                analyze_result = self.html_analyze.paser_xpath(html_content, xpath)
                self.result += analyze_result
                # print(analyze_result)
            except:
                pass
            # print(self.url_control_dil.has_new_url())
            time.sleep(1)

        # url='http://pdd.19mi.net/go/44174413'
        # html_content = self.download_html.download_html(url)
        # # print(html_content)
        # if not html_content:
        #     return False
        # xpath={
        #     'url':'//a/@href'
        # }
        # analyze_result = self.html_analyze.paser_xpath(html_content, xpath)
        # print(analyze_result)

        # print(self.result)
        return self.result

if __name__ == '__main__':
    a=panduoduo()
    a.start(["你好", "疯子"],1)
    # a=["你好","分子"]
    # print()