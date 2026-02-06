# THDORA Bot - Diccionarios Python

## 📋 Estructura de datos en memoria

Este documento define cómo se estructuran los diccionarios Python cuando se cargan los datos desde JSON.

---

## 👤 Diccionario: Usuario

**Variable:** `usuario`  
**Fuente:** `datos/usuario.json`

```python
usuario = {
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
# Nombre del usuario
nombre = usuario["nombre"]  # "Álvaro"

# Formato de hora preferido
formato = usuario["preferencias"]["formato_hora"]  # "24h"

# Total de citas creadas
total = usuario["estadisticas"]["total_citas"]  # 0

##🏷️ Diccionario: Categorías
Variable: categorias
Fuente: datos/categorias.json
categorias = {
    "estudio": {
        "emoji": "📚",
        "color": "azul"
    },
    "proyecto": {
        "emoji": "💻",
        "color": "verde"
    },
    "trabajo": {
        "emoji": "💼",
        "color": "gris"
    },
    "personal": {
        "emoji": "🏠",
        "color": "amarillo"
    },
    "deporte": {
        "emoji": "⚽",
        "color": "rojo"
    },
    "ocio": {
        "emoji": "🎮",
        "color": "morado"
    },
    "reunion": {
        "emoji": "👥",
        "color": "naranja"
    },
    "otros": {
        "emoji": "📌",
        "color": "negro"
    }
}
# Obtener emoji de una categoría
emoji = categorias["estudio"]["emoji"]  # "📚"

# Verificar si una categoría existe
if "deporte" in categorias:
    print("Categoría válida")

# Listar todas las categorías disponibles
lista_categorias = list(categorias.keys())
# ["estudio", "proyecto", "trabajo", ...]

##📅 Diccionario: Agenda (citas mensuales)
Variable: agenda
Fuente: datos/2026/febrero.json (ejemplo)
agenda = {
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
        },
        {
            "hora_inicio": "16:00",
            "hora_fin": "18:00",
            "nombre": "Primera función THDORA: agregar_cita()",
            "categoria": "proyecto"
        }
    ]
}
```

---

**Versión:** 1.0
**Última actualización:** 2026-02-04