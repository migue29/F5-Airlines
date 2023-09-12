from pymongo import MongoClient


# Conexión a MongoDB

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client["F5_Airlines"]
        if "F5_Airlines" not in client.list_database_names():
            db = client["F5_Airlines"]
            print("Base de datos creada correctamente")

        collection_name = "satisfaction_users"
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Colección '{collection_name}' creada correctamente")
        return db
   
    except Exception as e:
        print(f"Error al conectar a MongoDB: {str(e)}")
        return None

