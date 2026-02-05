"""
THDORA - Datos v0.3
Archivo: proyectos/thdora-bot/datos/thdora_data.py

Capa de datos con:
- Diccionario principal
- Agregar sesión (con cálculo auto de minutos)
- Ver sesiones
- Modificar sesión
- Eliminar sesión
- Buscar sesión

Pendiente para mañana:
- Guardar en JSON
- Cargar desde JSON
"""

from datetime import datetime

# ============================================
# DICCIONARIO PRINCIPAL
# ============================================

thdora_data = {
    'sesiones': []  # Lista vacía inicial
}

# CONCEPTO: Diccionario con lista dentro
# thdora_data['sesiones'] es una lista
# Podemos hacer: thdora_data['sesiones'].append(algo)

# ============================================
# CREAR SESIÓN
# ============================================

def agregar_sesion(nombre, hora_inicio, hora_fin):
    """
    Crea y agrega una sesión al diccionario
    
    Parámetros:
        nombre: str - Nombre de la actividad (ej: 'Musk', 'Médico', 'Gimnasio')
        hora_inicio: str - Formato 'HH:MM' (ej: '12:45')
        hora_fin: str - Formato 'HH:MM' (ej: '16:24')
    
    Retorna:
        dict - La sesión creada
    
    Ejemplo:
        >>> agregar_sesion('Musk', '12:45', '16:24')
        {'id': 1, 'nombre': 'Musk', 'hora_inicio': '12:45', 'hora_fin': '16:24', 'minutos': 219}
    """
    
    # Calcular minutos automáticamente
    inicio = datetime.strptime(hora_inicio, '%H:%M')
    fin = datetime.strptime(hora_fin, '%H:%M')
    diferencia = fin - inicio
    minutos = int(diferencia.total_seconds() / 60)
    
    # Crear diccionario de sesión
    sesion = {
        'id': len(thdora_data['sesiones']) + 1,  # ID automático
        'nombre': nombre,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'minutos': minutos  # AUTO-CALCULADO
    }
    
    # Agregar a la lista de sesiones
    thdora_data['sesiones'].append(sesion)
    
    return sesion

# ============================================
# LEER SESIONES
# ============================================

def ver_sesiones():
    """Muestra todas las sesiones en formato bonito"""
    
    if not thdora_data['sesiones']:
        print("📅 No hay sesiones registradas")
        return
    
    print("\n📅 SESIONES:")
    print("=" * 50)
    
    for s in thdora_data['sesiones']:
        print(f"{s['hora_inicio']}-{s['hora_fin']}: {s['nombre']} ({s['minutos']}min)")
    
    total = sum(s['minutos'] for s in thdora_data['sesiones'])
    print(f"\n⏱️  TOTAL: {total} min = {total/60:.1f}h")
    print("=" * 50)


def buscar_sesion(id_sesion):
    """
    Busca una sesión por ID
    
    Parámetros:
        id_sesion: int - ID de la sesión
    
    Retorna:
        dict o None - La sesión encontrada o None
    
    Ejemplo:
        >>> sesion = buscar_sesion(1)
        >>> print(sesion['nombre'])  # 'Musk'
    """
    for s in thdora_data['sesiones']:
        if s['id'] == id_sesion:
            return s
    return None

# ============================================
# ACTUALIZAR SESIÓN
# ============================================

def modificar_sesion(id_sesion, nuevo_nombre=None, nueva_hora_inicio=None, nueva_hora_fin=None):
    """
    Modifica campos de una sesión existente
    
    Parámetros:
        id_sesion: int - ID de la sesión a modificar
    
    Parámetros opcionales (solo modifica los que se pasen):
        nuevo_nombre: str
        nueva_hora_inicio: str
        nueva_hora_fin: str
    
    Retorna:
        bool - True si modificó, False si no encontró
    
    Ejemplo:
        >>> modificar_sesion(1, nuevo_nombre='Python')
        ✅ Sesión 1 modificada
        True
    """
    sesion = buscar_sesion(id_sesion)
    
    if sesion is None:
        print(f"❌ Sesión {id_sesion} no encontrada")
        return False
    
    # Modificar solo lo que se pasó
    if nuevo_nombre:
        sesion['nombre'] = nuevo_nombre
    
    if nueva_hora_inicio:
        sesion['hora_inicio'] = nueva_hora_inicio
    
    if nueva_hora_fin:
        sesion['hora_fin'] = nueva_hora_fin
    
    # Recalcular minutos si cambiaron horas
    if nueva_hora_inicio or nueva_hora_fin:
        inicio = datetime.strptime(sesion['hora_inicio'], '%H:%M')
        fin = datetime.strptime(sesion['hora_fin'], '%H:%M')
        diferencia = fin - inicio
        sesion['minutos'] = int(diferencia.total_seconds() / 60)
    
    print(f"✅ Sesión {id_sesion} modificada")
    return True

# ============================================
# ELIMINAR SESIÓN
# ============================================

def eliminar_sesion(id_sesion):
    """
    Elimina una sesión por ID
    
    Parámetros:
        id_sesion: int - ID de la sesión a eliminar
    
    Retorna:
        bool - True si eliminó, False si no encontró
    
    Ejemplo:
        >>> eliminar_sesion(3)
        🗑️  Sesión eliminada: Médico
        True
    """
    sesion = buscar_sesion(id_sesion)
    
    if sesion is None:
        print(f"❌ Sesión {id_sesion} no encontrada")
        return False
    
    thdora_data['sesiones'].remove(sesion)
    print(f"🗑️  Sesión eliminada: {sesion['nombre']}")
    return True

# ============================================
# ZONA DE PRUEBAS
# ============================================

if __name__ == "__main__":
    """
    Este bloque solo se ejecuta si haces:
    python datos/thdora_data.py
    
    NO se ejecuta si importas:
    from datos.thdora_data import agregar_sesion
    """
    
    print("\n🎯 PRUEBAS THDORA v0.3")
    print("=" * 50)
    
    # ========================================
    # TEST 1: Agregar sesiones del 5 de febrero
    # ========================================
    print("\n--- TEST 1: AGREGAR SESIONES ---")
    agregar_sesion('Musk', '12:45', '16:24')      # 219 min
    agregar_sesion('Siesta', '14:30', '15:30')    # 60 min
    agregar_sesion('Paseo Thea', '16:00', '17:00')  # 60 min
    agregar_sesion('ML', '19:00', '21:00')        # 120 min
    agregar_sesion('THDORA', '21:12', '22:09')    # 57 min
    print("✅ 5 sesiones agregadas")
    
    ver_sesiones()
    
    # ========================================
    # TEST 2: Modificar sesión
    # ========================================
    print("\n--- TEST 2: MODIFICAR SESIÓN ---")
    print("Cambiando 'Siesta' → 'Descanso'")
    modificar_sesion(2, nuevo_nombre='Descanso')
    ver_sesiones()
    
    # ========================================
    # TEST 3: Buscar sesión
    # ========================================
    print("\n--- TEST 3: BUSCAR SESIÓN ---")
    sesion = buscar_sesion(1)
    if sesion:
        print(f"✅ Encontrada: {sesion['nombre']} - {sesion['minutos']} min")
    
    # ========================================
    # TEST 4: Eliminar sesión
    # ========================================
    print("\n--- TEST 4: ELIMINAR SESIÓN ---")
    eliminar_sesion(3)  # Eliminar "Paseo Thea"
    ver_sesiones()
    
    # ========================================
    # TEST 5: Intentar eliminar inexistente
    # ========================================
    print("\n--- TEST 5: ELIMINAR INEXISTENTE ---")
    eliminar_sesion(99)
    
    # ========================================
    # RESUMEN
    # ========================================
    print("\n" + "=" * 50)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS")
    print("=" * 50)
    
    print("\n🔍 RESUMEN DEL DICCIONARIO:")
    print(f"Total sesiones actuales: {len(thdora_data['sesiones'])}")
    print(f"\nEstructura de una sesión:")
    if thdora_data['sesiones']:
        primera = thdora_data['sesiones'][0]
        for campo, valor in primera.items():
            print(f"  - {campo}: {valor} (tipo: {type(valor).__name__})")
    
    print("\n")
