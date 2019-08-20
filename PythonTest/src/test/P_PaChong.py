'''
Created on 2019年7月18日

@author: qiao.gu
'''
import urllib.request

class GetXueQiu(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.number = 0
    def function(self):
#         # 同花顺-个股行情
#         url = "http://q.10jqka.com.cn/"
#         response = urllib.request.urlopen(url)
#         print(response.read().decode('utf-8'))
#         print(type(response))
        # 同花财经-行情中心
        url = "http://quotes.money.163.com/old/#query=EQA&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0"
        response = urllib.request.urlopen(url)
        print(response.read().decode('utf-8'))
        print(type(response))
#         # 雪球-行情中心
#         url = "https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=90&order=desc&order_by=percent&exchange=CN&market=CN&type=sha&_=1563443941511"
#         response = urllib.request.urlopen(url)
#         print(response.read())
#         print(response.read().decode('utf-8'))
#         print(type(response))
        
test = GetXueQiu()
test.function()
        