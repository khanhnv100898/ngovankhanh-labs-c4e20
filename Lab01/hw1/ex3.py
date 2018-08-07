from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect
client = MongoClient(mongo_uri)

#get database
db = client.get_default_database()

#collection
posts = db['posts']

content="""Đố ai định nghĩa được tình yêu

Có nghĩa gì đâu, một buổi chiều

Nó chiếm hồn ta bằng nắng nhạt,

Bằng mây nhè nhẹ, gió hiu hiu ..."""   

#creat documents
new_post={
    "title": "Ngọc Bích Nguyễn",
    "author": "Nvkhanh",
    "content": content 
}

#insert
posts.insert_one(new_post)