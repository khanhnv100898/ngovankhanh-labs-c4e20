from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"

html_content = urlopen(url).read().decode('utf-8')
 
soup = BeautifulSoup(html_content,'html.parser')

section  = soup.find('section','section chart-grid')
# print(section.prettify())
li_list = section.find_all('li')

data = []
for li in li_list:
    list_itune = {}
    song  =li.h3.a
    singer = li.h4.a 
    # print(song,"\t ", singer)
    list_itune["Song"] = song.string
    list_itune["Singer"] = singer.string

    data.append(list_itune)

pyexcel.save_as(records = data , dest_file_name = "itune_songs.xlsx")

