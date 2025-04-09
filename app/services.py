import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
#para la autenticacion de la API simple
from functools import wraps
from flask import request, jsonify

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "taskmanager")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tasks")
API_KEY = os.getenv("API_KEY")


client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "No autorizado"}), 401
        
        token = auth_header.split(" ")[1]
        if token != API_KEY:
            return jsonify({"error": "Token inválido"}), 403

        return f(*args, **kwargs)
    return decorated

# Obtener todas las tareas
def get_all_tasks():
    tasks = list(collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

# Crear una nueva tarea
def create_task(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

# Actualizar una tarea (por ID)
def update_task(task_id, updates):
    result = collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": updates}
    )
    return result.modified_count

# Eliminar una tarea (por ID)
def delete_task(task_id):
    result = collection.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count
