from pymongo import MongoClient

client = MongoClient('localhost',27017) #Hecho la conexion con mongo
db= client.b2cveterinaria # CREO UNA BD
