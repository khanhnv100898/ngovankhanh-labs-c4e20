from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/HAG/IncSta/2018/2/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-hoang-anh-gia-lai.chn"

html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content,'html.parser')

div = soup.find('div','cf_ResearchDataHistoryInfo','tr')
# print(div.prettify())
td_list = div.find_all('td')

data =[]

for td in td_list:
    # list_td ={}
    name = td.string 
    print(name)
