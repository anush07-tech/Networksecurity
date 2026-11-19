from pymongo import MongoClient
uri = "mongodb+srv://anushnaik470_db_user:<db_password>@cluster0.4smamov.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)


