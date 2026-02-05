"""
THDORA - Datos MÍNIMOS v0.1
Archivo: proyectos/thdora-bot/datos/thdora_data.py

Solo lo esencial:
- Diccionario
- Agregar sesión
- Ver sesiones
(Sin JSON todavía, eso después)
"""
# ============================================
# PASO 1: EL DICCIONARIO
# ============================================
# El diccionario es nuestro 'almacen de datos'
# Todo vive aqui mientras el programa esta corriendo.
thdora_data = {
    'sesiones': [] #Lista vacia inicial de las sesiones.
}
# CONCEPTO: Diccionario con lista dentro
# thdora_data['sesiones'] es una lista
# Podemos hacer: thdora_data['sesiones'].append(algo)

# ============================================
# PASO 2: FUNCIÓN PARA AGREGAR SESIÓN
# ============================================

##def agregar_sesion(nombre, hora_inicio, hora_fin):