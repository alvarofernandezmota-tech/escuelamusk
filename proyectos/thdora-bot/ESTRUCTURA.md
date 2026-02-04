# THDORA Bot - Estructura de Datos

## 📁 Organización de archivos

```
datos/
├── usuario.json          ← Perfil del usuario
├── categorias.json       ← Categorías predefinidas
└── 2026/                 ← Citas por año
    ├── enero.json
    ├── febrero.json
    ├── marzo.json
    └── ...
```

---

## 👤 Estructura: `usuario.json`

**Propósito:** Almacenar datos del perfil del usuario

```json
{
  "nombre": "Álvaro",
  "zona_horaria": "Europe/Madrid",
  "creado_el": "2026-02-04",
  "preferencias": {
    "formato_hora": "24h",
    "idioma": "es"
  },
  "estadisticas": {
    "total_citas": 0,
    "categoria_favorita": ""
  }
}
```

### Campos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | string | Nombre del usuario |
| `zona_horaria` | string | Zona horaria (formato IANA) |
| `creado_el` | string | Fecha de creación del perfil (YYYY-MM-DD) |
| `preferencias.formato_hora` | string | Formato de hora: "24h" o "12h" |
| `preferencias.idioma` | string | Código de idioma (es, en, etc.) |
| `estadisticas.total_citas` | number | Total de citas creadas |
| `estadisticas.categoria_favorita` | string | Categoría más usada |

---

## 🏷️ Estructura: `categorias.json`

**Propósito:** Categorías predefinidas para clasificar citas

```json
{
  "categorias": [
    {
      "nombre": "estudio",
      "emoji": "📚",
      "color": "azul"
    },
    {
      "nombre": "proyecto",
      "emoji": "💻",
      "color": "verde"
    }
    // ... más categorías
  ]
}
```

### Categorías disponibles:

| Categoría | Emoji | Color | Uso recomendado |
|-----------|-------|-------|------------------|
| estudio | 📚 | azul | Clases, ejercicios, exámenes |
| proyecto | 💻 | verde | Desarrollo de proyectos |
| trabajo | 💼 | gris | Tareas laborales |
| personal | 🏠 | amarillo | Citas personales, familia |
| deporte | ⚽ | rojo | Ejercicio, entrenamiento |
| ocio | 🎮 | morado | Entretenimiento, hobbies |
| reunion | 👥 | naranja | Reuniones, videollamadas |
| otros | 📌 | negro | Cualquier otra actividad |

---

## 📅 Estructura: Citas mensuales (ej. `febrero.json`)

**Propósito:** Almacenar todas las citas de un mes específico

```json
{
  "04": [
    {
      "hora_inicio": "15:30",
      "hora_fin": "18:50",
      "nombre": "Estudiar Python - Ejercicios 8-15",
      "categoria": "estudio"
    },
    {
      "hora_inicio": "19:30",
      "hora_fin": "20:15",
      "nombre": "Planificación proyecto THDORA",
      "categoria": "proyecto"
    }
  ],
  "05": [
    {
      "hora_inicio": "10:00",
      "hora_fin": "11:30",
      "nombre": "Ver video funciones Python",
      "categoria": "estudio"
    }
  ]
}
```

### Estructura de cada día:

- **Clave:** Día del mes (`"01"` a `"31"`) en formato string de 2 dígitos
- **Valor:** Array de objetos (citas del día)

### Estructura de cada cita:

| Campo | Tipo | Formato | Validación | Descripción |
|-------|------|---------|-------------|-------------|
| `hora_inicio` | string | `"HH:MM"` | 00:00-23:59 | Hora de inicio (24h) |
| `hora_fin` | string | `"HH:MM"` | 00:00-23:59 | Hora de finalización |
| `nombre` | string | - | max 100 chars | Título/descripción de la cita |
| `categoria` | string | - | debe existir en `categorias.json` | Clasificación de la cita |

### Validaciones importantes:

✅ `hora_fin` debe ser posterior a `hora_inicio`  
✅ `categoria` debe existir en el archivo de categorías  
✅ El día debe ser válido según el mes (28-31)  
✅ Las horas deben estar en formato 24h (00:00 - 23:59)  

---

## 🛠️ Convenciones

### Formato de fechas:
- **Año:** Carpeta `2026/`
- **Mes:** Archivo `febrero.json` (nombre completo en minúsculas)
- **Día:** Clave `"04"` (string de 2 dígitos con cero a la izquierda)

### Formato de horas:
- **Sistema:** 24 horas
- **Formato:** `"HH:MM"` (string con ceros a la izquierda)
- **Ejemplos:** `"09:30"`, `"15:00"`, `"23:45"`

### Nombres de archivo:
- Meses en **español** y **minúsculas**
- Sin tildes: `enero.json`, `febrero.json`, `marzo.json`

---

## 📝 Ejemplos de uso

### Crear una cita:
```python
cita = {
    "hora_inicio": "14:00",
    "hora_fin": "15:30",
    "nombre": "Reunión con equipo",
    "categoria": "reunion"
}
```

### Añadir a un día existente:
```python
agenda["06"].append(cita)
```

### Crear un día nuevo:
```python
agenda["06"] = [cita]
```

---

## ⚠️ Consideraciones futuras

### Campos opcionales para v2.0:
- `prioridad`: "alta", "media", "baja"
- `recordatorio`: minutos antes de la cita
- `repeticion`: "ninguna", "diaria", "semanal", "mensual"
- `notas`: texto adicional
- `ubicacion`: lugar físico o URL
- `participantes`: lista de personas

### Migración a THEA IA:
Cuando se integre con THEA IA, esta estructura se mapeará a:
- **Usuario** → Tabla `users` (PostgreSQL)
- **Citas** → Tabla `events` (PostgreSQL)
- **Categorías** → Enum o tabla `categories`

---

**Versión:** 1.0  
**Última actualización:** 2026-02-04
