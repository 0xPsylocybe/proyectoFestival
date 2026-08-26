# Festival — Aplicación web

Aplicación web para **gestionar y consultar la programación** de un festival de música.
La usan tanto el público (consulta) como la organización (gestión de la programación).

## Descripción

La aplicación permite:

- Presentar el festival (nombre, fechas, ubicación, descripción, información para asistentes).
- Consultar el listado de **artistas** y la ficha detallada de cada uno (con sus géneros y actuaciones).
- Buscar artistas por nombre y filtrar por género musical.
- Consultar la **programación** completa: por día, por escenario y por artista.
- Gestionar (usuarios autorizados) artistas, géneros, escenarios y actuaciones desde la propia aplicación, sin editar la base de datos directamente.

Una actuación pertenece a un único artista y se realiza en un único escenario. Un escenario **no puede** tener dos actuaciones que empiecen a la misma hora; la aplicación debe impedirlo.

## Stack

- **Python** 3.14 · **Django** 6.1
- **Base de datos:** PostgreSQL (Supabase)
- Variables de entorno desacopladas de `settings.py` mediante `config/entorno.py` + `.env`

## Estructura del proyecto

```
proyectoFestival/
├── config/            # Proyecto Django (settings, urls, entorno.py)
│   ├── entorno.py     # Carga el .env (mantiene los secretos fuera de settings.py)
│   └── settings.py
├── core/              # Página inicial e información general del festival
├── artistas/          # Artistas y géneros (modelo, listado, ficha, búsqueda/filtrado)
├── actuaciones/       # Escenarios y actuaciones (programación, consultas, reglas)
├── .env               # Variables de entorno (NO se versiona)
├── .env.example       # Plantilla de variables de entorno
├── requirements.txt
└── manage.py
```

## Equipo y reparto de trabajo

| Módulo(s)                       | Responsable        |
| ------------------------------- | ------------------ |
| `core`, `artistas`             | **Luizay**         |
| `actuaciones` (escenarios + actuaciones) | **David** (davga) |

- **Luizay** — `core` y `artistas`: página de inicio e información del festival; modelo de artistas y géneros; listado, ficha del artista, buscador por nombre y filtro por género.
- **David** — `actuaciones` (escenarios + actuaciones): modelo de escenarios y actuaciones; programación completa; consultas por día / escenario / artista; regla de no solapamiento de actuaciones en un mismo escenario.

## Puesta en marcha

```bash
# 1. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar variables de entorno
copy .env.example .env       # y rellenar los valores (SECRET_KEY, credenciales de Supabase)

# 4. Aplicar migraciones
python manage.py migrate

# 5. Arrancar el servidor de desarrollo
python manage.py runserver
```

### Variables de entorno (`.env`)

| Variable        | Descripción                                    |
| --------------- | ---------------------------------------------- |
| `SECRET_KEY`    | Clave secreta de Django                        |
| `DEBUG`         | `True` en desarrollo, `False` en producción    |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por comas          |
| `DB_NAME`       | Nombre de la base de datos (Supabase)          |
| `DB_USER`       | Usuario de la base de datos                    |
| `DB_PASSWORD`   | Contraseña de la base de datos                 |
| `DB_HOST`       | Host del pooler de Supabase                    |
| `DB_PORT`       | Puerto (`5432`)                                |

> El archivo `.env` está excluido del control de versiones. Nunca subas credenciales al repositorio.

## Progreso

El seguimiento del trabajo y los próximos pasos están en [PROGRESO.md](PROGRESO.md).

## Repositorio

<https://github.com/0xPsylocybe/proyectoFestival> (privado)
