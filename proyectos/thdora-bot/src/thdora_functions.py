"""
THDORA - Funciones de gestión de citas
Fecha: 07 febrero 2026
Autor: Álvaro Fernández Mota

ESTRUCTURA DE DESARROLLO:
- Todas las funciones se implementan AQUI
- Todo el testing se hace en __main__
- Cada ejercicio se desarrolla directamente en este archivo
- Sin archivos separados de práctica (sin redundancia)

Progreso: 3/4 funciones base completadas ✅
"""

# ==========================================
# IMPORTS
# ==========================================
from thdora_data import thdora_data


# ==========================================
# EJERCICIO 2: AÑADIR CITA ✅ COMPLETADO
# ==========================================
def agregar_cita(nombre, fecha, hora_inicio, hora_fin):
    """
    Añade una nueva cita al diccionario thdora_data
    
    Args:
        nombre (str): Nombre de la cita
        fecha (str): Fecha formato YYYY-MM-DD
        hora_inicio (str): Hora inicio HH:MM
        hora_fin (str): Hora fin HH:MM
    
    Returns:
        dict: La cita creada
    
    Completado: 6 febrero 2026
    """
    nueva_cita = {
        'id': len(thdora_data['citas']) + 1,
        'nombre': nombre,
        'fecha': fecha,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
    }
    
    thdora_data['citas'].append(nueva_cita)
    return nueva_cita


# ==========================================
# EJERCICIO 3: VER CITAS ✅ COMPLETADO
# ==========================================
def ver_citas():
    """
    Muestra todas las citas guardadas en thdora_data
    Si no hay citas, muestra un mensaje informativo
    
    Returns:
        None: Imprime directamente en consola
    
    Completado: 6 febrero 2026
    """
    # Verificar si hay citas
    if len(thdora_data['citas']) == 0:
        print("❌ No hay citas registradas.")
        return
    
    # Mostrar cantidad de citas
    cantidad = len(thdora_data['citas'])
    print(f"\n📋 CITAS REGISTRADAS ({cantidad}):\n")
    
    # Recorrer y mostrar cada cita
    for cita in thdora_data['citas']:
        print(f"[{cita['id']}] {cita['nombre']}")
        print(f"    📅 {cita['fecha']}")
        print(f"    ⏰ {cita['hora_inicio']} - {cita['hora_fin']}")
        print()  # Línea en blanco entre citas


# ==========================================
# EJERCICIO 4: BUSCAR CITA ✅ COMPLETADO
# ==========================================
def buscar_cita(id):
    """
    Busca una cita por su ID y la muestra
    
    Args:
        id (int): ID de la cita a buscar
    
    Returns:
        dict: La cita encontrada, o None si no existe
    
    Completado: 7 febrero 2026
    """
    for cita in thdora_data['citas']:
        if cita['id'] == id:
            print(f"\n📌 CITA ENCONTRADA:")
            print(f"[{cita['id']}] {cita['nombre']}")
            print(f"    📅 {cita['fecha']}")
            print(f"    ⏰ {cita['hora_inicio']} - {cita['hora_fin']}")
            return cita
    
    print(f"❌ Cita con ID {id} no encontrada")
    return None


# ==========================================
# EJERCICIO 5: ELIMINAR CITA ⏳ PENDIENTE
# ==========================================
def eliminar_cita(id):
    """
    Elimina una cita por su ID
    
    Args:
        id (int): ID de la cita a eliminar
    
    Returns:
        bool: True si se eliminó, False si no existía
    
    TODO: Implementar en próxima sesión
    
    Pistas:
    - Recorrer thdora_data['citas'] con enumerate() para tener índice
    - Comparar cita['id'] con id buscado
    - Si encuentra: usar .pop(indice) para eliminar
    - Mostrar mensaje de confirmación
    - Si no encuentra: mensaje de error y return False
    """
    # Aquí irá tu código del ejercicio 5
    pass


# ==========================================
# TESTING COMPLETO - TODO EL PROYECTO AQUI
# ==========================================
if __name__ == "__main__":
    print("=" * 70)
    print("🧪 THDORA - TESTING COMPLETO DEL PROYECTO v0.3")
    print("=" * 70)
    print("Archivo: src/thdora_functions.py")
    print("Modo: Desarrollo activo - Todo se desarrolla aquí")
    print("Ejercicios: Se resuelven directamente en este archivo")
    print("=" * 70)
    
    # =========================================
    # TEST 1: VER CITAS VACÍO
    # =========================================
    print("\n" + "━" * 70)
    print("📍 TEST 1: ver_citas() - Lista vacía inicial")
    print("━" * 70)
    ver_citas()
    print("✅ Test 1 completado")
    
    # =========================================
    # TEST 2: AGREGAR CITAS (Ejercicio 2)
    # =========================================
    print("\n" + "━" * 70)
    print("📍 TEST 2: agregar_cita() - Ejercicio 2 ✅")
    print("━" * 70)
    
    print("\nAñadiendo cita 1...")
    cita1 = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    print(f"✅ Cita 1 añadida: {cita1['nombre']} (ID: {cita1['id']})")
    
    print("\nAñadiendo cita 2...")
    cita2 = agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    print(f"✅ Cita 2 añadida: {cita2['nombre']} (ID: {cita2['id']})")
    
    print("\nAñadiendo cita 3...")
    cita3 = agregar_cita("Gimnasio", "2026-02-13", "18:00", "19:00")
    print(f"✅ Cita 3 añadida: {cita3['nombre']} (ID: {cita3['id']})")
    
    print("\nAñadiendo cita 4...")
    cita4 = agregar_cita("Reunión equipo", "2026-02-14", "09:00", "10:30")
    print(f"✅ Cita 4 añadida: {cita4['nombre']} (ID: {cita4['id']})")
    
    print(f"\n📊 Total citas en memoria: {len(thdora_data['citas'])}")
    print("✅ Test 2 completado - Ejercicio 2 funciona correctamente")
    
    # =========================================
    # TEST 3: VER TODAS LAS CITAS (Ejercicio 3)
    # =========================================
    print("\n" + "━" * 70)
    print("📍 TEST 3: ver_citas() - Mostrar todas - Ejercicio 3 ✅")
    print("━" * 70)
    ver_citas()
    print("✅ Test 3 completado - Ejercicio 3 funciona correctamente")
    
    # =========================================
    # TEST 4: BUSCAR CITA EXISTENTE (Ejercicio 4)
    # =========================================
    print("━" * 70)
    print("📍 TEST 4: buscar_cita(2) - Buscar 'Estudiar Python' - Ejercicio 4 ✅")
    print("━" * 70)
    resultado = buscar_cita(2)
    if resultado:
        print(f"✅ Cita encontrada correctamente (ID: {resultado['id']})")
    print("✅ Test 4 completado - Ejercicio 4 funciona correctamente")
    
    # =========================================
    # TEST 5: BUSCAR OTRA CITA EXISTENTE
    # =========================================
    print("\n" + "━" * 70)
    print("📍 TEST 5: buscar_cita(1) - Buscar 'Dentista'")
    print("━" * 70)
    resultado = buscar_cita(1)
    if resultado:
        print(f"✅ Cita encontrada correctamente (ID: {resultado['id']})")
    print("✅ Test 5 completado")
    
    # =========================================
    # TEST 6: BUSCAR CITA INEXISTENTE
    # =========================================
    print("\n" + "━" * 70)
    print("📍 TEST 6: buscar_cita(999) - Buscar cita que NO existe")
    print("━" * 70)
    resultado = buscar_cita(999)
    if resultado is None:
        print("✅ Manejo correcto de cita inexistente (return None)")
    print("✅ Test 6 completado")
    
    # =========================================
    # TEST 7: ELIMINAR CITA (Ejercicio 5) ⏳
    # =========================================
    print("\n" + "━" * 70)
    print("📍 TEST 7: eliminar_cita(3) - Eliminar 'Gimnasio' - Ejercicio 5 ⏳")
    print("━" * 70)
    print("⚠️  PENDIENTE: Implementar eliminar_cita() en Ejercicio 5")
    print("Cuando implementes la función, descomenta este bloque:")
    print()
    print("# resultado = eliminar_cita(3)")
    print("# if resultado:")
    print("#     print('\\n📋 Citas después de eliminar:')")
    print("#     ver_citas()")
    print("#     print(f'✅ Cita eliminada. Total citas: {len(thdora_data[\"citas\"])}')
")
    
    # Descomenta estas líneas cuando implementes eliminar_cita():
    # resultado = eliminar_cita(3)
    # if resultado:
    #     print("\n📋 Citas después de eliminar:")
    #     ver_citas()
    #     print(f"✅ Cita eliminada. Total citas: {len(thdora_data['citas'])}")
    
    print("⏳ Test 7 pendiente - Completar en próxima sesión")
    
    # =========================================
    # RESUMEN FINAL
    # =========================================
    print("\n" + "=" * 70)
    print("📊 RESUMEN FINAL DEL PROYECTO")
    print("=" * 70)
    print(f"Total citas en memoria: {len(thdora_data['citas'])}")
    print(f"Funciones implementadas: 3/4 (75%)")
    print()
    print("Estado de ejercicios:")
    print("  ✅ Ejercicio 1: Diccionario base (thdora_data.py)")
    print("  ✅ Ejercicio 2: agregar_cita() - Completado 6 feb")
    print("  ✅ Ejercicio 3: ver_citas() - Completado 6 feb")
    print("  ✅ Ejercicio 4: buscar_cita() - Completado 7 feb")
    print("  ⏳ Ejercicio 5: eliminar_cita() - Pendiente")
    print()
    print("✅ Todos los tests implementados completados correctamente")
    print("=" * 70)
    print()
    print("🚀 PRÓXIMO PASO: Implementar eliminar_cita() en la línea 130")
    print("📝 Documentación completa en: docs/PROGRESO.md")
    print("=" * 70)
