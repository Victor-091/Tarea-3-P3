# CRUD API con Flask

API RESTful que implementa operaciones CRUD (Create, Read, Update, Delete) para gestión de usuarios.

## Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la API |
| POST | `/users` | Crear un nuevo usuario |
| GET | `/users` | Obtener todos los usuarios |
| GET | `/users/{id}` | Obtener un usuario por ID |
| PUT | `/users/{id}` | Actualizar un usuario |
| DELETE | `/users/{id}` | Eliminar un usuario |

## Ejemplos de uso

### Crear usuario
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Juan Perez","email":"juan@example.com"}'