# PLANWEDD
## Documentación del Back-end 
## Entorno virtual del proyecto primera vez

### Creación 

```sh
python -m venv venv
```

#### Activar

```sh
source venv/Scripts/activate -> Windows
source venv/bin/activate -> Linux / MacOS
```

### Dependencias

```python
pip install -r requirements.txt
```

#### Crear requirements (Ejecutar siempre que se instale una dependencia)

```python
pip freeze > requirements.txt
```

### Variables de Entorno
```
FLASK_ENV='development'
FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000

DATABASE_URI='postgresql://postgres:4268@localhost:5433/planwedd_db'

JWT_SECRET=[blocked]

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME='planweddservice@gmail.com'
MAIL_PASSWORD=[blocked]

CLOUD_NAME=[blocked]
API_KEY=[blocked]
API_SECRET=[blocked]
```

### Inicializar el proyecto en local en cualquier momento:
**1. Activar tu entorno virtual: **
`$ source venv/Scripts/activate`
**2. Actualizar la base de datos:**
`$ flask db upgrade`
**5.Acceso al objeto manejador de la base de dato de la semilla:**
`$ flask seed run`
**4.Iniciar el servidor de desarrollo:**
        `$ flask run`
> Nota: El usuario que se crea con el seed es
username: admin
password: 123456
y los roles que se crean son 2
1 administrador
2 usuario

###ENDPOINTS DE PLANWEDD

###Autenticación 
#### Rutas del módulo Autenticación
`POST  /auth/reset_password ` Resetear la constraseña de un usuario.
`POST  /auth/signin ` Crear token de autenticación.
`POST  /auth/signup ` Creación de usuarios.
`POST  /auth/token/refresh ` Obtener un nuevo access_token desde el refresh_token.

###Cuentas 
#### Rutas del módulo de Cuentas Bancarias
`GET  /baccounts ` Listar todas las cuentas.
`POST  /baccounts ` Creacción de cuenta.
`GET  /baccounts/{id} ` Obtener una cuenta por el ID.
`PUT  /baccounts/{id} ` Actualizar una cuenta por el ID.
`DELETE /baccounts/{id} ` Deshabilitar una cuenta por el ID.

###Dedicatorias 
#### Rutas del módulo de Dedicatorias
`GET  /dedications ` Listar todas las dedicatorias.
`POST  /dedications ` Creacción de dedicatorias.
`GET  /dedications/event{id} ` Obtener una dedicatoria por el ID del evento.
`GET  /dedications/{id} `  Obtener una dedicatoria por el ID.
`PUT  /dedications/{id} ` Actualizar una dedicatoria por el ID.
`DELETE /dedications/{id} ` Deshabilitar una dedicatoria por el ID.

###Eventos
#### Rutas del módulo de Eventos
`GET  /events ` Listar todos los eventos.
`POST  /events ` Creacción de eventos.
`GET  /events/{id} ` Obtener un evento por el ID.
`PUT  /events/{id} ` Actualizar un evento por el ID.
`DELETE /events/{id} ` Deshabilitar un evento por el ID.
`GET  /events/{id} ` Obtener un evento por el UserID.


###Regalos
#### Rutas del módulo de Regalos
`GET  /gifts ` Listar todos los regalos.
`POST  /gifts ` Creacción de regalos.
`GET  /gifts/events/{id} ` Obtener regalos por el ID del evento.
`POST  /gifts/soft` Creacción de regalos predeterminados.
`GET  /gifts/{id} ` Obtener un regalo por el ID.
`PUT  /gifts/{id} ` Actualizar un regalo por el ID.
`DELETE /gifts/{id} ` Deshabilitar un regalo por el ID.


###Roles
#### Rutas del módulo de Roles
`GET  /roles ` Listar todos los roles.
`POST  /roles ` Creacción de roles.
`GET  /roles/{id} ` Obtener un rol por el ID.
`PUT  /roles/{id} ` Actualizar un rol por el ID.
`DELETE /roles/{id} ` Deshabilitar un rol por el ID.


###Usuarios
#### Rutas del módulo de Usuarios
`GET  /users ` Listar todos los usuarios.
`POST  /users ` Creacción de usuarios.
`GET  /users/me ` Listar todos los usuarios.
`GET  /users/{id} ` Obtener un usuario por el ID.
`PUT  /users/{id} ` Actualizar un usuario por el ID.
`DELETE /users/{id} ` Deshabilitar un usuario por el ID.

##Modelado de Datos
`Auth SignIn{
username* string,
password* string
}`

`User Create{
nombres* string ,
apellidos* string,
dni* string,
username* string,
password* string,
correo*	 string,
rol_id	 integer,
}`

`Auth Reset Password{
correo*	string
}`

`Baccount Create{
banco string
nro_cuenta string
titular	string
usuario_id*	integer
}`


`Dedication Create{
nombre*	string
contenido*	string
evento_id*	integer
}`



`Event Update{
nombre_evento	string
fecha_evento	string
texto_portada	string
img_portada	string
configuraciones	string
}`

`Gift Create{
nombre*	string
descripcion	string
img_regalo	string
precio	string
evento_id*	integer
}`


`Gift Update{
nombre	string
descripcion	string
img_regalo	string
precio	string
}`

`Role Create{
name*	string
}`

`Role Update{
name*	string
}`

`User Update{
nombres	string
apellidos	string
dni	string
username	string
password	string
correo	string
}`


# Deploy en Heroku

## Logearse

```sh
heroku login
```

## Crear Aplicación

```sh
- heroku create -> Nombre random
- heroku create nombre_aplicacion -> Nombre a elección
```

## Agregar Variables de entorno

```sh
heroku config:set ENV=value
```

## Agregar PostgreSQL a la aplicación

```sh
heroku addons:create heroku-postgresql:hobby-dev
```

## Desplegar

```sh
git push heroku main
```

## Ejecutar migraciones

```sh
heroku run flask db upgrade
```

## Ejecutar seeders

```sh
heroku run flask db seed
```




