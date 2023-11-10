API de usuarios

Índice

Introducción: #introducción
Recursos: #recursos
Usuarios: #usuarios
Roles: #roles
Autenticación: #autenticación
Peticiones: #peticiones
Métodos: #metodos
Parámetros: #parametros
Respuestas: #respuestas
Formatos: #formatos
Códigos de estado: #codigos-de-estado
Errores: #errores
Licencia: #licencia
Introducción

Esta API REST proporciona acceso a los datos de los usuarios de una aplicación. Los recursos disponibles son los siguientes:

Usuarios: Representa a un usuario individual.
Roles: Representa un rol que puede asignarse a un usuario.
Recursos

Usuarios
El recurso /usuarios proporciona acceso a una lista de todos los usuarios.

Peticiones

Método: GET
Parámetros: Ninguno
Respuestas

Formato: JSON
JSON
[
  {
    "id": 1,
    "nombre": "Juan Pérez",
    "correo electrónico": "juan.perez@example.com",
    "rol": "administrador"
  },
  {
    "id": 2,
    "nombre": "María García",
    "correo electrónico": "maria.garcia@example.com",
    "rol": "usuario"
  }
]
Utiliza el código con precaución. Más información
Roles
El recurso /roles proporciona acceso a una lista de todos los roles.

Peticiones

Método: GET
Parámetros: Ninguno
Respuestas

Formato: JSON
JSON
[
  {
    "id": 1,
    "nombre": "administrador"
  },
  {
    "id": 2,
    "nombre": "usuario"
  }
]
Utiliza el código con precaución. Más información
Autenticación

Para acceder a la API, es necesario estar autenticado. La autenticación se realiza mediante el protocolo HTTP Basic.

Peticiones

Método: GET, POST, PUT, DELETE
Parámetros: Authorization
Respuestas

Código de estado: 401 (Unauthorized) si no se proporciona la autenticación o si es incorrecta.
Peticiones

La siguiente tabla muestra los métodos HTTP disponibles para cada recurso:

Recurso	Métodos
Usuarios	GET, POST, PUT, DELETE
Roles	GET, POST, PUT, DELETE
Parámetros

La siguiente tabla muestra los parámetros disponibles para cada método:

Recurso	Método	Parámetros
Usuarios	GET	Ninguno
Usuarios	POST	nombre, correo electrónico, rol
Usuarios	PUT	id, nombre, correo electrónico, rol
Usuarios	DELETE	id
Roles	GET	Ninguno
Roles	POST	nombre
Roles	PUT	id, nombre
Roles	DELETE	id
Respuestas

La siguiente tabla muestra los formatos de respuesta disponibles para cada recurso:

Recurso	Formato
Usuarios	JSON
Roles	JSON
Códigos de estado

La siguiente tabla muestra los códigos de estado HTTP que se pueden devolver por la API:

Código	Descripción
200	Operación realizada correctamente
400	Error en la solicitud
401	No autorizado
403	Prohibido
404	Recurso no encontrado
500	Error interno del servidor
Errores

La siguiente tabla muestra los errores específicos que se pueden devolver por la API:

Error	Descripción
Error de autenticación	La autenticación es incorrecta.
Error de autorización	No se tiene el permiso necesario para realizar la operación.
| `