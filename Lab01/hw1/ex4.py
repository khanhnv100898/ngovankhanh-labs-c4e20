from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect
client = MongoClient(mongo_uri)
#get database
db = client.get_default_database()
#collection
customers = db['customers']
#
all_customer = customers.find()

events = 0
wom = 0
ads = 0

for customer in all_customer:
    # first_customer = all_customer[i]
    if customer['ref'] == "events":
        events += 1
    elif customer['ref'] == "wom":
        wom += 1
    else:
        ads += 1

print("events",events)
print("wom",wom)
print("ads",ads)

#matplotlib
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#prepare data
labels = ['events','advertisements','word of mouth']
values=[events,ads,wom]
colors =['green','blue','orange']
explode=[0,0,0]
#plot
pyplot.pie(values, labels=labels,colors=colors,explode=explode)
pyplot.axis('equal')
#show
pyplot.show()