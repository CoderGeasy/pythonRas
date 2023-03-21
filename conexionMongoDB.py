from pymongo import MongoClient
import pymongo


class ConexionMongoDB:
    def __init__(self):
        self.db = ""
        self.cluster = "mongodb+srv://admin:televicion05@cluster0.uujrdgs.mongodb.net/?retryWrites=true&w=majority"

    def conectarBD(self):
        try:
            client = MongoClient(self.cluster)
            client.server_info()
            print("Conexión exitosa")
            self.db = client['Sensores-Raspberry']
            return True
        except Exception:
            print("No hay conexion a la base de datos, revisa tu conexion a internet!")
            return False

    def insertar(self, collection_nombre, datos):
        collection = self.db[collection_nombre]
        collection.insert_one(datos)

    def cerrarConexion(self):
        self.client.close()
