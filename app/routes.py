from flask import Blueprint, request, jsonify
from app.services import get_all_tasks, create_task, update_task, delete_task, require_auth
from flask_cors import cross_origin

import uuid


task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/tasks', methods=['GET'])
@cross_origin()
def get_tasks():
    """
    Obtener todas las tareas
    ---
    tags:
      - Tareas
    responses:
      200:
        description: Lista de tareas
        schema:
          type: array
          items:
            properties:
              _id:
                type: string
              title:
                type: string
              description:
                type: string
              status:
                type: string
    """
    print("📥 Entrando a GET /tasks")
    try:
        tasks = get_all_tasks()
        print("✅ Tareas recuperadas:", tasks)
        return jsonify(tasks), 200
    except Exception as e:
        print("❌ Error al obtener tareas:", str(e))
        return jsonify({"error": str(e)}), 500
    #return jsonify(get_all_tasks())


@task_routes.route('/tasks', methods=['POST'])
@require_auth
def post_task():
    """
    Crear una nueva tarea
    ---
    tags:
      - Tareas
    parameters:
      - in: body
        name: tarea
        required: true
        schema:
          properties:
            title:
              type: string
              example: Comprar leche
            description:
              type: string
              example: Ir al super
    responses:
      201:
        description: Tarea creada exitosamente
      401:
        description: No autorizado
    """
    data = request.get_json()
    new_task = {
        "title": data.get("title"),
        "description": data.get("description", ""),
        "status": "por hacer"
    }
    task_id = create_task(new_task)
    new_task["_id"] = task_id
    return jsonify(new_task), 201

@task_routes.route('/tasks/<task_id>', methods=['PUT'])
@require_auth
def put_task(task_id):
    """
    Actualizar una tarea por ID
    ---
    tags:
      - Tareas
    parameters:
      - name: task_id
        in: path
        type: string
        required: true
        description: ID de la tarea a actualizar
      - in: body
        name: datos
        required: true
        description: Campos a actualizar
        schema:
          properties:
            status:
              type: string
              example: en progreso
              enum: [por hacer, en progreso, completada]
            description:
              type: string
              example: Actualizado desde Swagger
            title:
              type: string
              example: Tarea modificada
    responses:
      200:
        description: Tarea actualizada exitosamente
      401:
        description: No autorizado
      403:
        description: Token inválido
      404:
        description: Tarea no encontrada
      422:
        description: Estado inválido
    """
    data = request.get_json()
    updates = {}
    # Validar y agregar campos permitidos
    if "status" in data:
        if data["status"] not in ["por hacer", "en progreso", "completada"]:
            return jsonify({"error": "Estado inválido"}), 422
        updates["status"] = data["status"]

    if "description" in data:
        updates["description"] = data["description"]

    if "title" in data:
        updates["title"] = data["title"]

    if not updates:
        return jsonify({"error": "Nada para actualizar"}), 400

    updated = update_task(task_id, updates)

    if updated:
        return jsonify({"message": "Tarea actualizada"}), 200
    else:
        return jsonify({"error": "Tarea no encontrada"}), 404


@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
@require_auth
def delete_task_by_id(task_id):
    """
    Eliminar una tarea por ID
    ---
    tags:
      - Tareas
    parameters:
      - name: task_id
        in: path
        type: string
        required: true
        description: ID de la tarea a eliminar
    responses:
      200:
        description: Tarea eliminada exitosamente
      401:
        description: No autorizado
      403:
        description: Token inválido
      404:
        description: Tarea no encontrada
    """
    deleted = delete_task(task_id)

    if deleted:
        return jsonify({"message": "Tarea eliminada"}), 200
    else:
        return jsonify({"error": "Tarea no encontrada"}), 404

