from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect
client = MongoClient(mongo_uri)

#get database
db = client.get_default_database()

#collection
posts = db['posts']

#
all_post = posts.find()
# for i in range(10):
#     first_post = all_post[i]
#     print(first_post['title'])
#     print(first_post['author'])
#     print(first_post['content'])
for post in all_post:
    print(post['title'])
    print(post['author'])
    print(post['content'])



