# Proyecto Patrimonio

Aplicación web en Django para explorar lugares patrimoniales por categoría y consultar sus detalles.

## Requisitos

- Python 3.12 o posterior.
- pip.

La aplicación usa Django 6.1.2 y SQLite. No requiere instalar ni configurar un servidor de base de datos aparte.

## Instalación

Desde la raíz del repositorio, crea y activa un entorno virtual:

En Windows (PowerShell):

```powershell
python -m venv .venv
```

Permitir la ejecución de scripts en PowerShell (Solo en Windows si aparece error de directivas):
Si al intentar activar el entorno recibes un error sobre Execution Policy, ejecuta

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias del proyecto:

```bash
python -m pip install -r requirements.txt
```

## Base de datos

La configuración predeterminada utiliza SQLite. Desde el directorio del proyecto Django (`ProyectoPatrimonio/`), aplica las migraciones para crear o actualizar `db.sqlite3`:

```bash
cd ProyectoPatrimonio
python manage.py migrate
```

Para administrar el contenido desde Django admin, crea un usuario:

```bash
python manage.py createsuperuser
```

## Ejecutar la aplicación

Desde `ProyectoPatrimonio/`, inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> para ver el sitio y <http://127.0.0.1:8000/admin/> para administrar los datos.

En el admin, las imágenes de los lugares se ingresan como URL. Usa una URL pública que apunte directamente a una imagen.

## Pruebas

Desde `ProyectoPatrimonio/`, ejecuta:

```bash
python manage.py test
```
