from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#1. Download web page
url = 'http://dantri.com.vn'
#1.1 create connection 
# conn = urlopen(url)
#1.2 read
# data = conn.read()
# print(data)
#1.3 Decode
# html_content = data.decode('utf-8')
html_content = urlopen(url).read().decode('utf-8')
# print(html_content)

#save html to file

# import urllib.request    
# urllib.request.urlretrieve("http://dantri.com.vn", "dantri.html")

# f = open('dantri.html','wb')
# f.write(html_content)
# f.close()



#2. Extract ROI (Region Of Interest)
#html, xml, xhtml
soup = BeautifulSoup(html_content, 'html.parser')

# print(soup.prettify())

ul = soup.find('ul','ul1 ulnew')
# print(ul.prettify())




#3. Extract data
li_list = ul.find_all('li')


data =[ ]

for li in li_list:
    # li = li_list[0]
    # print(li.prettify())
    # h4 = li.h4
    # a = h4.a
    post = {}
    a = li.h4.a
    # print(a)
    post['title']= a.string
    post['url'] = url + a['href']

    data.append(post)

    # print(a.string)
    # print(url + a['href'])
    # print("* " *30)


pyexcel.save_as(records=data, dest_file_name="data_dantri.xlsx")