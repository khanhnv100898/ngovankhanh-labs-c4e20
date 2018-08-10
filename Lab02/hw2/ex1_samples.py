from youtube_dl import YoutubeDL

#1 Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=tN8dQRItsLQ']) #EM CHẲNG THỂ BIẾT (#YNKHHIT) - T | OFFICIAL MV LYRICS | ViruSs

#2 Download multiple youtube videos
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=HowNWSBFRI0','https://www.youtube.com/watch?v=kRvYqzCJ4vw']) #[ Lyric Video ] Em Là Lý Do Anh Say • B-Ray ft ViruSs#LẠ LÙNG - VŨ [OFFICIAL]

#3 Download audio
options = {
    'format' : 'bestaudio/audio'
}
d1 = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=7ChKIKGFLno']) #Lemaitre - Higher (ft. Maty Noyes)

#4 Search and then download the first video
options ={
    'default_search' : 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['điều khác lạ'])

#5 Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format' : 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['buồn không em masew'])