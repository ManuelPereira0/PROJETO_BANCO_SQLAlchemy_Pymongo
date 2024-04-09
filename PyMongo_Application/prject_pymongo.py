import datetime
import pprint
from pymongo import *

client = MongoClient('localhost', 27017)

db = client.test
colletion = db.test_collection

posts = db.conta

post = [{
    "name" : "Manuel",
    "cpf" : "01234567890",
    "endereco": "Rua ABC",
    "conta" : "0000000 - 1",
    "agencia" : "0000",
    "tipo" : "Poupança"
},
{
   "name" : "Fernanda",
    "cpf" : "09876543210",
    "endereco": "Rua XZY",
    "conta" : "0000000 - 2",
    "agencia" : "0001",
    "tipo" : "Salário"             
},
{
    "name" : "Claudio",
    "cpf" : "74102589632",
    "endereco": "Rua VENASD",
    "conta" : "0000000 - 3",
    "agencia" : "0002",
    "tipo" : "Corrente"  
}]

result = posts.insert_many(post)

for post in posts.find():
    pprint.pprint(post)
    
posts.delete_one({"name" : "Manuel"})


