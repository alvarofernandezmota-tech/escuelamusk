# THDORA Bot - Estructura del Proyecto

## 📁 Organización de carpetas

```
proyectos/thdora-bot/
├── README.md                  ← Overview del proyecto
├── ROADMAP.md                 ← Plan de desarrollo
├── LICENSE                    ← Licencia MIT
├── .gitignore                 ← Git ignore
├── main.py                    ← Interfaz CLI (Fase 2)
│
├── docs/                      ← Documentación completa
│   ├── conceptos/             ← Teoría Python
│   │   ├── README.md
│   │   ├── diccionarios.md
│   │   ├── listas.md
│   │   ├── funciones.md
│   │   └── datetime.md
│   │
│   ├── ejercicios/            ← Ejercicios paso a paso
│   │   ├── README.md          ← Índice de ejercicios
│   │   ├── 01-diccionario-base.md
│   │   ├── 02-agregar-cita.md
│   │   ├── 03-ver-citas.md
│   │   └── ... (más ejercicios)
│   │
│   ├── arquitectura/          ← Diseño del sistema
│   │   ├── estructura-proyecto.md  ← Este archivo
│   │   ├── estructura-datos.md
│   │   └── fases-desarrollo.md
│   │
│   └── sesiones/              ← Diario de desarrollo
│       ├── README.md
│       └── 2026-02-06-reorganizacion.md
│
├── src/                       ← Código fuente
│   ├── __init__.py
│   ├── thdora_data.py         ← Diccionario + funciones
│   │
│   └── snapshots/             ← Progreso documentado
│       ├── README.md
│       ├── v01_diccionario.py
│       ├── v02_agregar.py
│       ├── v03_ver.py
│       └── ... (más versiones)
│
├── datos/                     ← Persistencia JSON (Fase 2)
│   ├── .gitkeep
│   ├── thdora.json            ← Datos principales
│   └── backup/
│       └── thdora_backup_*.json
│
└── tests/                     ← Testing (Fase 3)
    ├── __init__.py
    └── test_thdora.py
```

---

## 📝 Descripción de carpetas

### 📄 Raíz del proyecto

| Archivo | Propósito |
|---------|----------|
| `README.md` | Documentación principal del proyecto |
| `ROADMAP.md` | Plan de desarrollo y progreso |
| `main.py` | Punto de entrada (interfaz CLI) |
| `LICENSE` | Licencia open source (MIT) |
| `.gitignore` | Archivos ignorados por Git |

---

### 📚 `docs/` - Documentación

Toda la documentación del proyecto separada del código.

#### `docs/conceptos/`
Teoría y explicaciones de conceptos Python:
- Diccionarios y listas
- Funciones
- Manejo de archivos
- Fechas con datetime

#### `docs/ejercicios/`
Ejercicios paso a paso para construir THDORA:
- Cada ejercicio = un concepto Python
- Incluye especificaciones, solución y testing
- Progreso documentado

#### `docs/arquitectura/`
Diseño y arquitectura del sistema:
- Estructura de carpetas
- Estructura de datos
- Plan de fases

#### `docs/sesiones/`
Diario de desarrollo:
- Sesión por día
- Logros y aprendizajes
- Reflexiones

---

### 💻 `src/` - Código fuente

Todo el código Python ejecutable.

#### `src/thdora_data.py`
Archivo principal que contiene:
- Diccionario base `thdora_data`
- Funciones principales (agregar, ver, buscar, etc.)
- Lógica del negocio

#### `src/snapshots/`
Capturas del código en cada etapa:
- `v01_diccionario.py` - Después del ejercicio 1
- `v02_agregar.py` - Después del ejercicio 2
- `v03_ver.py` - Después del ejercicio 3
- ...

**Utilidad:**
- Ver evolución del proyecto
- Comparar versiones
- Referenciar estados anteriores

---

### 💾 `datos/` - Persistencia (Fase 2)

**Estado:** ⏳ Se creará en Ejercicio 7 (guardar_json)

#### `datos/thdora.json`
Archivo JSON principal con todos los datos:
```json
{
  "citas": [
    {
      "id": 1,
      "titulo": "Dentista",
      "fecha": "2026-02-10",
      "hora": "10:00",
      "descripcion": "Revisión anual"
    }
  ]
}
```

#### `datos/backup/`
Backups automáticos:
- `thdora_backup_20260206_1730.json`
- `thdora_backup_20260206_2015.json`
- ...

---

### 🧪 `tests/` - Testing (Fase 3)

**Estado:** ⏳ Se creará en Fase 3

Tests automatizados:
- `test_thdora.py` - Tests unitarios
- Testing de todas las funciones
- Validación de datos

---

## 📊 Evolución de la estructura

### Versión 0.1 (Actual)
```
✓ docs/
✓ src/
✓ src/snapshots/
× datos/
× tests/
```

### Versión 0.2 (Ejercicio 7)
```
✓ docs/
✓ src/
✓ src/snapshots/
✓ datos/          ← NUEVO
× tests/
```

### Versión 0.3 (Fase 3)
```
✓ docs/
✓ src/
✓ src/snapshots/
✓ datos/
✓ tests/          ← NUEVO
```

---

## 🔍 Convenciones

### Nombres de archivos
- **Markdown:** `kebab-case.md` (estructura-proyecto.md)
- **Python:** `snake_case.py` (thdora_data.py)
- **JSON:** `snake_case.json` (thdora.json)

### Estructura de commits
```
🏗️ Reorganización estructura
✅ Ejercicio 1: Diccionario base
📝 Actualizar README
🐛 Fix: error en agregar_cita
✨ Feat: nueva función buscar_cita
```

### Snapshots
Formato: `vXX_descripcion.py`
- `v01_diccionario.py`
- `v02_agregar.py`
- `v03_ver.py`

---

## 🚀 Relación con Git

```
.gitignore contendrá:
__pycache__/
*.pyc
.env
datos/backup/*
!datos/backup/.gitkeep
```

---

**Versión:** 2.0  
**Última actualización:** 6 febrero 2026  
**Autor:** Álvaro Fernández Mota