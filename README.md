# Task Manager API - Backend (Python + Flask + MongoDB + AWS Lambda)

Este proyecto es parte del reto técnico para la posición de Fullstack Developer (React + Python Serverless) en Seek.  
La API permite gestionar tareas para un equipo de desarrollo, con operaciones CRUD, autenticación por token, y despliegue serverless vía AWS Lambda.

---

## Tecnologías usadas

- **Python 3.9**
- **Flask**
- **MongoDB (Atlas)**
- **Docker / Docker Compose**
- **Pytest**
- **AWS Lambda + ECR**
- **Swagger UI (Flasgger)**

---

## Funcionalidades

- [x] Crear tarea (`POST /tasks`)
- [x] Listar todas las tareas (`GET /tasks`)
- [x] Actualizar estado, descripción o título de una tarea (`PUT /tasks/<id>`)
- [x] Eliminar tarea (`DELETE /tasks/<id>`)
- [x] Autenticación por token
- [x] Validaciones básicas
- [x] Documentación Swagger en `/apidocs`
- [x] Pruebas automatizadas con `pytest`

---

## Cómo levantar el proyecto en local

1. Clona el repositorio:

```bash
git clone https://github.com/odmoreno/task-manager-api.git
cd task-manager-api
```

2. Crea un .env

3. Levanta los servicios con Docker:

```bash
docker-compose up --build

```

4. Accede a la API desde:
   http://localhost:5000/tasks

5. Documentación interactiva Swagger:
   http://localhost:5000/apidocs

## Cómo correr las pruebas

```bash
docker-compose exec <container_id> pytest

```
