# 2026-02-04 – Trabajo en THDORA Bot (Sesión 19:30 - 22:18)

## 1. Objetivo de la sesión

- Definir la **estructura de datos y carpetas** del bot de agenda personal THDORA.
- Crear los primeros **archivos JSON** (usuario, categorías, plantilla de citas mensuales).
- Empezar a programar el **`main.py`** del bot con menú y saludo personalizado.
- Practicar el flujo de trabajo con **Git** específico de este proyecto.

---

## 2. Estructura de carpetas y archivos

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
ESTRUCTURA.md

Describe la organización de datos/ y los formatos de:

usuario.json → perfil del usuario.

categorias.json → categorías de citas.

2026/febrero.json → citas por día del mes.

Define convenciones:

Fechas por año/carpeta, mes/archivo, día/clave "DD".

Horas en formato HH:MM 24h.

Meses en español y minúsculas (ej. febrero.json).

README.md

Introducción al bot THDORA.

Idea general: asistente de agenda personal en consola para gestionar citas.

ROADMAP.md

Lista de futuras funcionalidades:

Añadir/editar/eliminar citas.

Ver citas por día y por mes.

Filtrado por categoría.

Estadísticas básicas.

DICCIONARIOS.md

“Chuleta” de uso de diccionarios en Python aplicada a THDORA:

Agenda como dict de días → lista de citas.

Ejemplos de:

Crear un día nuevo.

Añadir una cita a un día existente.

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

Guardar el nombre del usuario para poder mostrar un saludo personalizado.

Incluir zona_horaria y formato_hora pensando en una versión futura más avanzada.

Dejar preparado estadisticas para métricas (total de citas, categoría favorita).

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

nombre: identificador interno (lo que se guarda en cada cita).

emoji: icono visual para mostrar en listados.

color: pensado para futuras interfaces más visuales.

datos/2026/febrero.json
Ejemplo actual:

json
{
  "04": [
    {
      "hora_inicio": "15:30",
      "hora_fin": "18:50",
      "nombre": "Estudiar Python - Ejercicios 8-15 estructuras datos",
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
Clave: "DD" (día en 2 dígitos).

Valor: lista de citas, donde cada cita tiene:

hora_inicio, hora_fin, nombre, categoria.

Nota: más adelante se podría evolucionar a un objeto por día (citas, reflexion, habitos), pero eso se deja como idea futura, no implementada todavía.

2.3. Módulos Python
funciones/__init__.py

Archivo vacío para que proyectos/thdora-bot pueda tratarse como paquete Python en el editor/IDE.

3. Lógica del bot en main.py
3.1. Importaciones
python
import json
Se importa json porque THDORA leerá los datos desde los archivos JSON (usuario.json, etc.).

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
Primer diseño del menú, con las 6 acciones básicas que tendrá el bot.

Por ahora, todas las opciones se marcan como [FUNCIONALIDAD EN DESARROLLO] en el cuerpo de main().

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
Encapsula la lógica de:

Leer el JSON de usuario.

Mostrar un saludo bonito con el nombre.

Devolver nombre_usuario para poder reutilizarlo (por ejemplo, al despedirse).

Uso de with open(..., encoding="utf-8") para soportar tildes y emojis.

3.4. Bucle principal main()
Versión actual:

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
Decisiones tomadas:

agenda = {} será el diccionario en memoria para sincronizar con los archivos mensuales más adelante.

Un único while True gobierna el flujo:

Muestra el menú.

Pide una opción al usuario.

Llama a la acción correspondiente (de momento, solo mensajes de “en desarrollo”).

Pendientes claros para próximas sesiones:

Sustituir el print de bienvenida genérico por:

python
nombre_usuario = saludar_usuario()
Convertir la despedida en un f-string para que use el nombre real:

python
print(f"\n👋 Hasta pronto, {nombre_usuario}! Tus citas están guardadas.")
4. Trabajo con Git específico de THDORA
Durante la sesión he usado Git de forma sistemática:

Comprobar estado

bash
git status
Para ver:

Archivos modificados (proyectos/thdora-bot/main.py, etc.).

Archivos nuevos (ESTRUCTURA.md, DICCIONARIOS.md, usuario.json, etc.).

Añadir archivos relevantes

bash
git add proyectos/thdora-bot/main.py
git add proyectos/thdora-bot/ESTRUCTURA.md
git add proyectos/thdora-bot/DICCIONARIOS.md
git add proyectos/thdora-bot/README.md
git add proyectos/thdora-bot/ROADMAP.md
git add proyectos/thdora-bot/datos/usuario.json
git add proyectos/thdora-bot/datos/categorias.json
Commits con mensajes claros

docs: Crear documentación de diccionarios Python

feat: Saludo personalizado y despedida con nombre en THDORA

fix: Añadir __init__.py a proyectos para VS Code

Subir a GitHub

bash
git push origin main
Limpieza de “ruidos”

Apareció un archivo accidental tatusa:

Detectado con git status como “Untracked file”.

Eliminado con del tatusa para dejar el árbol limpio.

Estado final de la sesión:

text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
5. Ideas futuras y decisiones tomadas hoy
Reflexión diaria en la agenda:

Idea: que cada día no solo tenga citas, sino también un campo reflexion con una frase corta sobre cómo ha ido el día.

Ejemplo futuro:

json
"04": {
  "citas": [ ... ],
  "reflexion": "Día muy centrado en Python y en empezar a dar forma a THDORA."
}
Decisión: solo lo dejo diseñado; todavía no lo implemento en el código.

Hábitos diarios y análisis semanal:

Idea: por cada día guardar un bloque habitos con checks true/false (leer, deporte, meditar, etc.) y luego hacer análisis semanal.

Decisión de hoy:

No implementar todavía hábitos hasta avanzar más con el curso de Python.

Dejarlo como mejora futura en el ROADMAP para una v2 del bot.

Organización por meses vs semanas:

Confirmado que es suficiente y más simple guardar los datos por meses (2026/febrero.json) y derivar la vista semanal en código.

No hace falta cambiar la estructura de archivos a semanas.

6. Resumen de la sesión
He definido y documentado la estructura de datos del bot:

Perfil de usuario.

Categorías predefinidas.

Citas mensuales por día.

He creado el esqueleto del código Python:

Menú principal (mostrar_menu).

Primera función real de negocio (saludar_usuario leyendo JSON).

Bucle main() que controlará el flujo general del bot.

He usado Git como parte natural del trabajo, con varios commits pequeños, y he dejado el repositorio limpio al cerrar la sesión.

He dejado diseñadas, pero no implementadas aún, las ideas de:

Reflexión diaria dentro del JSON de agenda.

Bloque de hábitos diarios y posible análisis semanal.