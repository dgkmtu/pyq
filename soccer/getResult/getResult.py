from urllib.request import urlopen
from bs4 import BeautifulSoup

Iurl = "C:\\Users\\yinag\\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\getResult\\url.txt"
with open(Iurl, mode='r', encoding='utf-8-sig') as f:
    for row in f:
        column = row.rstrip()
        print(column)

html = urlopen(column)

bs = BeautifulSoup(html, 'html.parser')

#nameList = bs.find_all('section', {'class':'matchlistWrap'})
#nameList = bs.find_all('table', {'class':'gameTable'})
#nameList = bs.find_all('td',{'class':{'stadium','match'}})
#nameList = bs.find_all([['div', {'class':{'leagAccTit'}}], ['td', {'class':{'stadium','match'}}]])
nameList = bs.find_all(,{'class':'leagAccTit'})
for name in nameList:
    print(name.get_text())

