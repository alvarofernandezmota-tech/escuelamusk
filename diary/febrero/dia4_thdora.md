# 2026-02-04 – Trabajo en THDORA Bot (Sesión 19:30 - 22:18)

## 1. Objetivo de la sesión

- Definir la **estructura de datos y carpetas** del bot de agenda personal THDORA.
- Crear los primeros **archivos JSON** (usuario, categorías, plantilla de citas mensuales).
- Empezar a programar el **`main.py`** del bot con menú y saludo personalizado.
- Practicar el flujo de trabajo con **Git** específico de este proyecto.

---

## 2. Estructura de carpetas y archivos creada

Ruta base del proyecto:

```text
proyectos/
└── thdora-bot/
    ├── ESTRUCTURA.md
    ├── README.md
    ├── ROADMAP.md
    ├── DICCIONARIOS.md
    ├── datos/
    │   ├── usuario.json
    │   ├── categorias.json
    │   └── 2026/
    │       ├── .gitkeep
    │       └── febrero.json
    ├── funciones/
    │   └── __init__.py
    └── main.py
2.1. Documentación del proyecto
ESTRUCTURA.md:

Describe la organización de datos/ y los formatos de:

usuario.json (perfil del usuario).

categorias.json (categorías de citas).

2026/febrero.json (citas por día del mes).[cite:191]

Define convenciones:

Fechas por año/carpeta, mes/archivo, día/clave "DD".

Horas en formato HH:MM 24h.

Nombres de archivos de mes en español y minúsculas.

README.md:

Introducción al bot THDORA.

Idea general: asistente de agenda personal en consola.

ROADMAP.md:

Lista de futuras funcionalidades: gestión de citas, filtros por día/mes, categorías, estadísticas, etc.

DICCIONARIOS.md:

Pequeña “chuleta” de diccionarios en Python aplicada al bot:

Agenda como dict de días → lista de citas.

Ejemplos de acceso y actualización (añadir cita a un día, crear día nuevo).

2.2. Archivos de datos (datos/)
datos/usuario.json
json
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
Decisiones:

Guardar el nombre del usuario para poder saludarlo.

Guardar zona_horaria y formato_hora pensando en una futura versión con fechas/horas más avanzadas.

estadisticas preparado para futuras métricas: total de citas y categoría más usada.[cite:190]

datos/categorias.json
json
{
  "categorias": [
    { "nombre": "estudio",  "emoji": "📚", "color": "azul" },
    { "nombre": "proyecto", "emoji": "💻", "color": "verde" },
    { "nombre": "trabajo",  "emoji": "💼", "color": "gris" },
    { "nombre": "personal", "emoji": "🏠", "color": "amarillo" },
    { "nombre": "deporte",  "emoji": "⚽", "color": "rojo" },
    { "nombre": "ocio",     "emoji": "🎮", "color": "morado" },
    { "nombre": "reunion",  "emoji": "👥", "color": "naranja" },
    { "nombre": "otros",    "emoji": "📌", "color": "negro" }
  ]
}
Cada categoría tiene:

nombre: clave interna que se usará en las citas ("estudio", "proyecto", etc.).

emoji: icono visual para mostrar en listados.

color: idea de paleta si algún día se presenta en UI más rica.[cite:189]

datos/2026/febrero.json
Archivo preparado para guardar las citas de febrero 2026.

Formato documentado en ESTRUCTURA.md:

Clave: "DD" (día en 2 dígitos).

Valor: lista de citas con campos:

hora_inicio, hora_fin, nombre, categoria.[cite:191]

Se deja como plantilla para futuras sesiones (todavía sin lógica en el código).

2.3. Módulos Python
funciones/__init__.py:

Archivo vacío para que proyectos/thdora-bot se pueda tratar como paquete Python desde VS Code/IDE.

3. Lógica del bot en main.py
3.1. Importaciones
python
import json
Se importa json porque el bot va a leer datos de datos/usuario.json (y más adelante de otros JSON).[cite:187]

3.2. Menú principal
python
def mostrar_menu():
    """
    Muestra el menú principal de THDORA
    """
    print("\n" + "="*50)
    print(" " * 15 + "THDORA BOT 📅")
    print(" " * 10 + "Gestión de Agenda Personal")
    print("="*50)
    print("\n1. Agregar cita")
    print("2. Ver citas del día")
    print("3. Ver citas del mes")
    print("4. Eliminar cita")
    print("5. Buscar cita")
    print("6. Salir")
    print("\n" + "-"*50)
Primer diseño del menú con 6 opciones básicas.

Todas las opciones por ahora muestran solo [FUNCIONALIDAD EN DESARROLLO]; servirán como anclaje para funciones futuras.[cite:187]

3.3. Función saludar_usuario()
python
def saludar_usuario():
    """
    Carga el usuario y muestra saludo personalizado.
    Devuelve el nombre del usuario.
    """
    with open("datos/usuario.json", "r", encoding="utf-8") as file:
        usuario = json.load(file)
    
    nombre_usuario = usuario["nombre"]
    
    print("\n" + "="*50)
    print(f"👋 ¡Hola {nombre_usuario}! Bienvenido a THDORA")
    print("🗓️  Tu asistente de agenda personal")
    print("="*50)
    
    return nombre_usuario
Primero contacto con funciones “reales” en el bot:

Encapsula la lógica de leer el JSON del usuario.

Devuelve nombre_usuario para poder usarlo en otras partes del programa (por ejemplo, al despedirse).[cite:187]

Decisiones:

Uso de with open(..., encoding="utf-8") para soportar caracteres especiales (tildes, emojis).

Guardar el resultado de json.load(file) en un diccionario usuario y extraer la clave "nombre".

3.4. Bucle principal main()
python
def main():
    """
    Función principal del bot
    """
    # Diccionario en memoria para las citas (luego lo cargaremos de JSON)
    agenda = {}
    
    print("\n🚀 Bienvenido a THDORA - Tu asistente de agenda personal")
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()
        
        if opcion == "1":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a agregar_cita(agenda)
            
        elif opcion == "2":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a mostrar_citas_dia(agenda)
            
        elif opcion == "3":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a mostrar_citas_mes(agenda)
            
        elif opcion == "4":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a eliminar_cita(agenda)
            
        elif opcion == "5":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a buscar_cita(agenda)
            
        elif opcion == "6":
            print("\n👋 Hasta pronto, {nombre_usuario}! Tus citas están guardadas.")
            # Aquí llamaremos a guardar_datos(agenda)
            break
            
        else:
            print("\n❌ Opción inválida. Por favor, elige del 1 al 6.")
Decisiones de diseño:

agenda = {} preparado como diccionario en memoria que luego se sincronizará con datos/2026/febrero.json.

Un solo bucle while True que:

Muestra menú.

Lee opción del usuario.

Ejecuta la acción correspondiente.

Pendientes para próximas sesiones:

Sustituir el saludo genérico por llamada real a saludar_usuario() y guardar el nombre:

nombre_usuario = saludar_usuario().

Convertir la despedida en un f-string para que se use el nombre real:

print(f"\n👋 Hasta pronto, {nombre_usuario}! ...").[cite:187]

4. Trabajo con Git específico de THDORA
Durante esta sesión se han hecho varios pasos siguiendo siempre el mismo patrón:

Comprobar el estado:

git status para ver:

Archivos modificados (proyectos/thdora-bot/main.py).

Archivos nuevos (proyectos/thdora-bot/...).

Añadir archivos relevantes:

git add proyectos/thdora-bot/main.py

git add proyectos/thdora-bot/ESTRUCTURA.md

git add proyectos/thdora-bot/DICCIONARIOS.md

git add proyectos/thdora-bot/README.md

git add proyectos/thdora-bot/ROADMAP.md

git add proyectos/thdora-bot/datos/usuario.json

git add proyectos/thdora-bot/datos/categorias.json

Crear commits con mensajes claros:

"docs: Crear documentación de diccionarios Python"

"feat: Saludo personalizado y despedida con nombre en THDORA"

"fix: Añadir __init__.py a proyectos para VS Code"

Subir a GitHub:

git push origin main

Resolver pequeños “ruidos”:

Aparición de un archivo accidental tatusa:

Detectado con git status como “Untracked file”.

Eliminado con del tatusa para dejar el árbol limpio.

Resultado final de la sesión:

text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
5. Resumen de la sesión de trabajo en THDORA
He definido y documentado la estructura de datos del bot:

Perfil de usuario.

Categorías predefinidas.

Formato de citas diarias/mensuales.

He creado el esqueleto del código Python:

Menú principal (mostrar_menu).

Primera función real de negocio (saludar_usuario leyendo JSON).

Bucle main() que controlará todo el flujo del bot.

He usado Git como parte natural del trabajo:

Pensando ya en commits pequeños, claros y en dejar el repositorio siempre limpio al terminar la sesión.

Esta sesión deja THDORA listo para, en próximas sesiones, empezar a implementar las operaciones reales sobre la agenda: agregar citas, listarlas por día/mes y guardarlas en los archivos JSON.