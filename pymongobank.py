import pprint
import pymongo as pyM

client = pyM.MongoClient(
    "mongodb+srv://lukaspymongo:pymongotest@pymongo0.7p2yl9n.mongodb.net/?retryWrites=true&w=majority&appName=PyMongo0"
)
db = client.challenge
collection = db.dio_collection
print(db.list_collection)


post1 = {
    "name":"Lukas Maximo",
    "cpf":"999.999.999-99",
    "address":"lukasmaximo@gmail.com",
    "account":[
        {
            "kind":"Conta Corrente",
            "agency":"0001",
            "number":33,
            "saldo":200.00
        },
        {
            "kind":"Poupança",
            "agency":"0001",
            "number":51,
            "saldo":1000.00
        }
    ]
}

post2 = {
    "name":"Samuel Tarly",
    "cpf":"009.990.091-23",
    "address":"lukasmaximo@gmail.com",
    "account":[
        {
            "kind":"Conta Corrente",
            "agency":"0002",
            "number":33,
            "saldo":250.00
        },
        {
            "kind":"Conta Corrente",
            "agency":"0001",
            "number":33,
            "saldo":7500.00
        }
    ]
}

post3 = {
    "name":"Patrick Star",
    "cpf":"012.101.232-10",
    "address":"lukasmaximo@gmail.com",
    "account":[
        {
            "kind":"Conta Corrente",
            "agency":"0002",
            "number":33,
            "saldo":75.00
        },
        {
            "kind":"Cheque Especial",
            "agency":"0002",
            "number":13,
            "saldo":1000000000.00
        }
    ]
}

posts = db.posts
post_id = posts.insert_one(post1).inserted_id
print(post_id)
post_id = posts.insert_one(post2).inserted_id
print(post_id)
post_id = posts.insert_one(post3).inserted_id
print(post_id)
print(db.posts.find_one())
for p in db.posts.find():
    pprint.pprint(p)

print("============================")
for p in db.posts.find({"name":"Patrick Star"}):
    pprint.pprint(p)
print("============================")
for p in db.posts.find({"account.agency":"0001"}):
    pprint.pprint(p)

collections = db.list_collection_names()
for collection in collections:
    db[collection].drop()