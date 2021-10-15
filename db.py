import pymongo

client = pymongo.MongoClient('mongodb://localhost/bestboyfriendbot')
users_db = client.get_database()["users_db"]
