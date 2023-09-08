from pymongo import MongoClient


# Conexión a MongoDB

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client["F5_Airlines"]
        return db
   
    except Exception as e:
        print(f"Error al conectar a MongoDB: {str(e)}")
        return None

