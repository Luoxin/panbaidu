

from pan115 import pan115
from panduoduo import panduoduo
from tuoniao import tuoniao
from wangpan56 import wangpan56

import json

import sys
sys.path.append("../yunpan")
sys.path.append('..')
from yunpan import SearchServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class AggregateSearch:
    def __init__(self):
        self.search_engine = [pan115(),tuoniao(), panduoduo(), wangpan56(),]
        self.result = []
        keywords = []
        index = 1

    def getSocketResponse(self,keyword, index = 1):
        print(json.loads(keyword),index)
        self.__search(json.loads(keyword), index)

        return json.dumps(self.result)

        # return "aaa"

    def __search(self,keywords, index = 1):
        for model in self.search_engine:
            try:
                print("正在{}上搜索".format(model))
                result = model.start(keywords, index)
                # print(result)
                if isinstance(result, list):
                    self.result += result
            except:
                pass

        # print(self.result)

        # self.thread_count = self.search_engine.__len__()
        # self.thread = []
        #
        # for thread_count in range(self.thread_count):
        #     self.thread.append(Thread(None, self.search_engine[thread_count].start(keywords, index=1)))
        #     self.thread[thread_count].daemon = True
        #     self.thread[thread_count].start()

if __name__ == '__main__':
    handler = AggregateSearch()
    processor = SearchServer.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1', 30303)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting python server...")
    server.serve()
