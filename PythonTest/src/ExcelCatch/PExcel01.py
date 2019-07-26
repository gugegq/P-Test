'''
Created on 2019年7月1日

@author: qiao.gu
'''

from re import findall
from urllib.request import urlopen
from openpyxl import Workbook

url = r'https://xueqiu.com/hq'
with urlopen(url, '', 10) as fp:
    content = fp.read().decode()
    
pattern = r'<tr>' + r'(.|\n)*?<td>(.*?)</td>' *3 + r'(.|\n)*?</tr>'
result = findall(pattern, content)

wb = Workbook()
ws = wb.worksheets[0]

for line in result:
    line = [line[1], line[3], line[5]]
    ws.append(line)
    
wb.save('test.xlsx')