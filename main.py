import sys
import json
sys.path.append('./gen-py')

from yunpan import SearchServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol



def search(keywords, index = 1):
    try:
        print("由于目前为单线程本地操作，请来耐心等待查询结果······")
        # Make socket
        transport = TSocket.TSocket('127.0.0.1', 30303)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = SearchServer.Client(protocol)
        transport.open()
        keywords = json.dumps(keywords)

        msg = json.loads(client.getSocketResponse(keywords, index))

        result = {}

        for val in msg:
            result[val['url']] = val['title']

        file = open("result.txt","w")
        for key,val in result.items():
            print(val, "   ", key)
            file.writelines(str(val)+"   "+str(key)+"\n")
        file.close()
        transport.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if len(sys.argv) > 1 :
        keywords = sys.argv[1:]
        search(keywords)
    else:
        print("请输入要查询的关键字： ",end="")
        keywords = input()
        search(keywords.split(" "))
