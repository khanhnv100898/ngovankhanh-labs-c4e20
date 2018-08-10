from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

html_content = urlopen(url).read().decode('utf-8')
 
soup = BeautifulSoup(html_content,'html.parser')

section  = soup.find('section','section chart-grid')
li_list = section.find_all('li')

options ={
    'default_search' : 'ytsearch',
    'max_downloads': 1
}

dl = YoutubeDL(options)

for li in li_list:
    song  =li.h3.a
    singer = li.h4.a
    search_1 = song.string + " " + singer.string
    dl.download([search_1])
