from download_html import HtmlDownloader as html_downloader
from html_analyze import HtmlParser as html_parser
from url_controller import UrlControl as url_control

import urllib.parse


class tuoniao:
    def __init__(self):

        self.download_html = html_downloader()  # 下载器
        self.html_analyze = html_parser()  # 解析器
        self.url_control_dil = url_control()  # 存储详情页
        pass

    def start(self,keywords,index=1):
        key=" ".join(keywords)
        # print(key, urllib.parse(key))
        url = 'http://www.tuoniao.me/Web/search/'
        # print(url)
        try:
            post_dict={
                'q': key,
                'find': 2,
                'sort': 2,
                'page': 1,
            }
            headers_dict = {
               'Accept': 'application / json, text / plain, * / *',
                'Host': 'www.tuoniao.me',
                'Referer': "http://www.tuoniao.me/search/{}/list".format(urllib.parse.quote(key)),
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
            }
            self.download_html.set_headers(headers_dict)
            html_content = self.download_html.download_post_json(url, post_dict)
            # print(html_content)
            result_title = []
            result_url = []
            for __,val in enumerate(html_content['results']):
                result_title.append(val['title'])
                result_url.append(val['link'])

            result = {
                'title':result_title,
                'url': result_url,
            }
            xpath = {
                'reorganization':['title','url'],
            }
            result = self.html_analyze.list_to_dict(result, xpath)
            # print(result)
            return result
        except:
            pass





if __name__ == '__main__':
    a=tuoniao()
    a.start(["你好", "疯子"], 1)

