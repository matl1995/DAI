import pymongo

# Connection to Mongo DB
conn=pymongo.MongoClient()
db = conn.restaurantes
restaurantes_c=db.restaurants