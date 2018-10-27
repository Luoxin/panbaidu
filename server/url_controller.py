
class UrlControl(object):
    '''
    用于url管理的类
    '''
    def __init__(self):
        self.__new_urls=set()  # 需要继续抓取的url
        self.__old_urls=set()  # 已经抓取完成的url

    def add_new_url(self, root_url):
        '''
        增加一个新的url
        :param root_url:
        :return:
        '''
        if root_url not in self.__new_urls and root_url not in self.__old_urls:
            self.__new_urls.add(root_url)

    def has_new_url(self):
        '''
        判断是否存在未抓取的url
        :return:
        '''
        return self.__new_urls.__len__()>0

    def get_new_url(self):
        '''
        得到一个为抓取的url并将此url移至已抓取
        :return:
        '''
        new_url=self.__new_urls.pop()
        # self.__old_urls.add(new_url)
        return new_url

    def add_new_urls(self, new_urls):
        '''
        增加一组带抓取的url
        :param new_urls:
        :return:
        '''
        for url in new_urls:
            self.add_new_url(url)

    def add_old_url(self,old_url):
        '''
        增加不需要抓取的url
        :param old_url:
        :return:
        '''
        if old_url in self.__new_urls:
            self.__new_urls.remove(old_url)
        if old_url not in self.__old_urls:
            self.__old_urls.add(old_url)

    def add_old_urls(self,old_urls):
        '''
        增加一组不需要抓取的url
        :param old_urls:
        :return:
        '''
        for url in old_urls:
            self.add_old_url(url)

    def get_new_urls_len(self):
        '''
        返回带抓取的url个数
        :return:
        '''
        return self.__new_urls.__len__()

    def get_old_urls_len(self):
        '''
        返回已抓取和不需要抓取的url个数
        :return:
        '''
        return self.__old_urls.__len__()