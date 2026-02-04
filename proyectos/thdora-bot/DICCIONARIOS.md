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
Operaciones comunes:
1. Agregar una cita nueva a un día existente:
python
nueva_cita = {
    "hora_inicio": "14:00",
    "hora_fin": "15:00",
    "nombre": "Reunión con equipo",
    "categoria": "reunion"
}

agenda["04"].append(nueva_cita)
2. Crear un día nuevo con una cita:
python
agenda["06"] = [
    {
        "hora_inicio": "09:00",
        "hora_fin": "10:00",
        "nombre": "Ejercicio matutino",
        "categoria": "deporte"
    }
]
3. Verificar si un día tiene citas:
python
if "07" in agenda:
    print(f"El día 7 tiene {len(agenda['07'])} citas")
else:
    print("El día 7 no tiene citas")
4. Recorrer todas las citas de un día:
python
for cita in agenda["04"]:
    print(f"{cita['hora_inicio']} - {cita['nombre']}")
5. Recorrer todos los días del mes:
python
for dia, citas in agenda.items():
    print(f"Día {dia}: {len(citas)} citas")
    for cita in citas:
        print(f"  - {cita['hora_inicio']}: {cita['nombre']}")
        🔄 Conversión JSON ↔ Python
Cargar desde JSON:
python
import json

# Cargar usuario
with open("datos/usuario.json", "r", encoding="utf-8") as file:
    usuario = json.load(file)

# Cargar categorías
with open("datos/categorias.json", "r", encoding="utf-8") as file:
    datos = json.load(file)
    categorias = datos["categorias"]  # Convertir lista a diccionario

# Cargar agenda de febrero
with open("datos/2026/febrero.json", "r", encoding="utf-8") as file:
    agenda = json.load(file)
Guardar a JSON:
python
import json

# Guardar agenda
with open("datos/2026/febrero.json", "w", encoding="utf-8") as file:
    json.dump(agenda, file, ensure_ascii=False, indent=2)

# Guardar usuario
with open("datos/usuario.json", "w", encoding="utf-8") as file:
    json.dump(usuario, file, ensure_ascii=False, indent=2)
📝 Notas importantes
Días como strings: Los días se guardan como "04", "05" (strings con cero a la izquierda), no como números.

Horas formato 24h: Siempre en formato "HH:MM" (string).

Categorías válidas: Antes de usar una categoría, verificar que existe en el diccionario categorias.

Encoding UTF-8: Siempre usar encoding="utf-8" al leer/escribir archivos para soportar emojis y caracteres especiales.

indent=2 en JSON: Para que los archivos JSON sean legibles al guardarlos.

Versión: 1.0
Última actualización: 2026-02-04