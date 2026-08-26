# Progreso del proyecto

Seguimiento del estado del proyecto y de los próximos pasos por módulo.

Leyenda: ✅ hecho · 🔄 en curso · ⬜ pendiente

---

## Estado general

| Módulo        | Responsable | Estado |
| ------------- | ----------- | ------ |
| Configuración | Común       | ✅     |
| `core`        | Luizay      | ⬜     |
| `artistas`    | Luizay      | ⬜     |
| `actuaciones` | David       | 🔄     |

---

## Modelo de datos acordado

Cuatro modelos de dominio (2 de Luizay, 2 de David). La información del festival
es **estática** en `core` (un único festival, sin modelo). La autenticación usa el
`auth` de Django + grupo "Organización" (sin modelo nuevo). El M:N Artista–Género
lo gestiona Django con su tabla puente automática (no se modela a mano).

| App | Modelo | Campos | Reglas |
| --- | ------ | ------ | ------ |
| `artistas` | `Genero` | nombre (único) | — |
| `artistas` | `Artista` | nombre (indexado), imagen, descripción, procedencia · M:N → Genero | Reglas 5 y 6 |
| `actuaciones` | `Escenario` | nombre (único), ubicación, capacidad | — |
| `actuaciones` | `Actuacion` | artista (FK), escenario (FK), fecha (indexada), hora_inicio, duracion_minutos | Reglas 1–4 y **7**: `unique(escenario, fecha, hora_inicio)` |

```
Genero  N ──M  Artista  1 ──N  Actuacion  N── 1  Escenario
```

---

## Configuración inicial (común) ✅

- [x] Proyecto Django `config` con las apps `core`, `artistas` y `actuaciones`
- [x] Variables de entorno desacopladas (`config/entorno.py` + `.env`)
- [x] Base de datos PostgreSQL (Supabase) conectada
- [x] Migraciones iniciales de Django aplicadas
- [x] Modelos de las 3 apps migrados a Supabase (Generos, Artistas, Escenario, Actuacion)
- [x] Repositorio en GitHub y README

---

## Luizay — `core` y `artistas`

### `core` (información del festival)
- [ ] Información del festival como contenido estático (nombre, fechas, ubicación, descripción, info para asistentes) — sin modelo
- [ ] Página de inicio con la presentación del festival
- [ ] Sección de información general
- [ ] Navegación hacia programación y resto de secciones

### `artistas` (artistas y géneros)
- [ ] Modelo `Genero`
- [ ] Modelo `Artista` (nombre, imagen, descripción, procedencia) con relación M:N a géneros
- [ ] Listado de artistas
- [ ] Ficha de detalle del artista (datos + sus actuaciones)
- [ ] Búsqueda por nombre
- [ ] Filtro por género musical
- [ ] Registro en el admin de Django

---

## David — `actuaciones` (escenarios + actuaciones)

### Escenarios
- [x] Modelo `Escenario` (nombre, ubicación en el recinto, capacidad)
- [x] Listado de escenarios (view + URL + plantilla)
- [x] Gestión de escenarios (alta/edición/baja) protegida con `@gestor_required`

### Actuaciones
- [x] Modelo `Actuacion` (artista, escenario, fecha, hora de comienzo, duración aproximada)
- [x] **Regla:** impedir dos actuaciones que empiecen a la misma hora en el mismo escenario (constraint BD + `clean()`)
- [x] Programación completa (vista pública `programacion`)
- [x] Consulta de actuaciones por día (filtro GET)
- [x] Consulta de actuaciones por escenario (filtro GET)
- [x] Consulta de actuaciones por artista (filtro GET)
- [x] Gestión de actuaciones (añadir / modificar / eliminar) protegida con `@gestor_required`
- [x] Registro en el admin de Django
- [x] Feedback con `messages` en las operaciones de gestión

---

## Transversal (a coordinar entre ambos)

- [~] Autenticación y permisos: visitante (solo consulta) vs. organización (gestión)
  - [x] Login/logout cableados (`cuentas/login`, `cuentas/logout`) + `LOGIN_URL`/redirects
  - [x] Plantilla `registration/login.html`
  - [x] Decorador `gestor_required` + filtro `is_gestor` aplicados en la app de David
  - [x] Superusuario creado
  - [ ] Grupo "Gestores" en el admin (para gestores que no sean superusuario)
  - [x] Enlaces login/logout en la navbar (logout por POST) — Luizay
- [x] Mensajes de resultado en las operaciones de gestión (vistas + render en `base.html`)
- [x] Sistema de estilos: `static/css/base.css` (paleta Bosque & Bermellón), enlazado desde `base.html`
- [x] `base.html` con bloques `title`/`contenido`, navbar y footer — Luizay
- [x] Datos de prueba (script idempotente cargado en Supabase)
  - [ ] Convertir el script en fixture/comando versionado

---

## Verificación (app de David)

### Automática — hecha ✅
- [x] Regla 7: bloquea solapamiento con mensaje claro; deja pasar las que no solapan
- [x] Programación: renderiza las 6 actuaciones, ordenadas, con país y fecha en español
- [x] Filtro por día
- [x] Filtro combinado (día + escenario) → AND correcto
- [x] Listado de escenarios con recuento de actuaciones correcto
- [x] Protección: anónimo no accede a gestión (302); login responde 200

### Manual — pendiente (flujo autenticado, probar como gestor)
- [ ] Con sesión iniciada, en Programación y Escenarios aparecen "Nuevo…" y Editar/Eliminar
- [ ] Crear escenario → vuelve al listado y sale mensaje verde de éxito
- [ ] Crear actuación en Escenario Principal el 2026-07-17 a las 22:30 → rechazada con el error de la Regla 7 en el formulario
- [ ] Editar y eliminar una actuación → mensajes correspondientes

---

## Próximos pasos (opcionales, app de David)

1. Ficha de escenario (detalle con sus actuaciones).
2. Convertir los datos de prueba en fixture/comando versionado.
3. Pulido visual de programación y formularios.

### Notas / a coordinar con Luizay
- `gestor_required` redirige a `inicio` en vez de a `login` (un anónimo va a la home, no al login). Cambiar `login_url="login"` si se quiere.
- Decidido: sistema de estilos propio (no Bootstrap). Bootstrap CSS sigue enlazado en `base.html`; retirarlo requiere sustituir las clases de layout y revisar las plantillas de core.
