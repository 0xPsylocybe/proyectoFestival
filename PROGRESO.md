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
- [~] Plantilla `escenario_list.html` (falta view + URL)
- [~] Plantilla de gestión `escenario_form.html` (falta view + form + URL)
- [ ] Gestión de escenarios (alta/edición/baja) desde la aplicación

### Actuaciones
- [x] Modelo `Actuacion` (artista, escenario, fecha, hora de comienzo, duración aproximada)
- [x] **Regla:** impedir dos actuaciones que empiecen a la misma hora en el mismo escenario (constraint BD + `clean()`)
- [~] Plantilla de gestión `actuacion_form.html` (falta view + form + URL)
- [ ] Programación completa (vista cómoda con muchas actuaciones)
- [ ] Consulta de actuaciones por día
- [ ] Consulta de actuaciones por escenario
- [ ] Consulta de actuaciones por artista
- [ ] Gestión de actuaciones (añadir / modificar / eliminar) desde la aplicación
- [ ] Registro en el admin de Django

---

## Transversal (a coordinar entre ambos)

- [ ] Autenticación y permisos: visitante (solo consulta) vs. organización (gestión)
- [ ] Mensajes de resultado en las operaciones de gestión
- [ ] Plantillas base y estilos comunes
- [ ] Datos de prueba / fixtures

---

## Próximos pasos inmediatos

1. **Bloqueo:** `Actuacion.artista` referencia `artistas.Artista`, que aún no existe. Hasta que Luizay defina `Artista` y `Genero`, no se puede pasar `check`/`makemigrations`.
2. Luizay crea los modelos `Genero` y `Artista` en su app.
3. Generar migraciones de todos los modelos y aplicarlas a Supabase.
4. Registrar los modelos en el admin para poder cargar datos de prueba.
