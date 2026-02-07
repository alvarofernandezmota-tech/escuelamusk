"""
THDORA - Funciones de gestión de citas
Fecha: 07 febrero 2026
Autor: Álvaro Fernández Mota

Funciones disponibles:
- agregar_cita(): Añade nueva cita
- ver_citas(): Muestra todas las citas
- buscar_cita(): Busca cita por ID
- eliminar_cita(): Elimina cita por ID (pendiente)

Progreso: 3/4 funciones base completadas ✅
"""

# ==========================================
# IMPORTS
# ==========================================
from thdora_data import thdora_data


# ==========================================
# FUNCIÓN: AÑADIR CITA
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
    
    Ejemplo:
        >>> agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
        {'id': 1, 'nombre': 'Dentista', 'fecha': '2026-02-10', ...}
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
# FUNCIÓN: VER CITAS
# ==========================================
def ver_citas():
    """
    Muestra todas las citas guardadas en thdora_data
    Si no hay citas, muestra un mensaje informativo
    
    Returns:
        None: Imprime directamente en consola
    
    Ejemplo:
        >>> ver_citas()
        
        📋 CITAS REGISTRADAS (2):
        
        [1] Dentista
            📅 2026-02-10
            ⏰ 10:00 - 11:00
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
# FUNCIÓN: BUSCAR CITA POR ID
# ==========================================
def buscar_cita(id):
    """
    Busca una cita por su ID y la muestra
    
    Args:
        id (int): ID de la cita a buscar
    
    Returns:
        dict: La cita encontrada, o None si no existe
    
    Ejemplo:
        >>> buscar_cita(1)
        
        📌 CITA ENCONTRADA:
        [1] Dentista
            📅 2026-02-10
            ⏰ 10:00 - 11:00
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
# FUNCIÓN: ELIMINAR CITA POR ID
# ==========================================
def eliminar_cita(id):
    """
    Elimina una cita por su ID
    
    Args:
        id (int): ID de la cita a eliminar
    
    Returns:
        bool: True si se eliminó, False si no existía
    
    Ejemplo:
        >>> eliminar_cita(1)
        ✅ Cita con ID 1 eliminada correctamente
    """
    # TODO: Implementar en ejercicio 5
    # Pista: Recorrer thdora_data['citas'], encontrar por id, usar .remove()
    pass


# ==========================================
# TESTING COMPLETO - Desarrollo activo
# ==========================================
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TESTING THDORA FUNCTIONS v0.3")
    print("=" * 60)
    print("Archivo: src/thdora_functions.py")
    print("Modo: Desarrollo con testing activo")
    print("=" * 60)
    
    # TEST 1: Ver citas vacío
    print("\n📍 TEST 1: ver_citas() - Lista vacía")
    print("-" * 60)
    ver_citas()
    
    # TEST 2: Agregar citas
    print("\n📍 TEST 2: agregar_cita() - Añadir 4 citas")
    print("-" * 60)
    cita1 = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    print(f"✅ Cita 1 añadida: {cita1['nombre']} (ID: {cita1['id']})")
    
    cita2 = agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    print(f"✅ Cita 2 añadida: {cita2['nombre']} (ID: {cita2['id']})")
    
    cita3 = agregar_cita("Gimnasio", "2026-02-13", "18:00", "19:00")
    print(f"✅ Cita 3 añadida: {cita3['nombre']} (ID: {cita3['id']})")
    
    cita4 = agregar_cita("Reunión equipo", "2026-02-14", "09:00", "10:30")
    print(f"✅ Cita 4 añadida: {cita4['nombre']} (ID: {cita4['id']})")
    
    # TEST 3: Ver todas las citas
    print("\n📍 TEST 3: ver_citas() - Mostrar todas (4 citas)")
    print("-" * 60)
    ver_citas()
    
    # TEST 4: Buscar cita existente
    print("📍 TEST 4: buscar_cita(2) - Buscar 'Estudiar Python'")
    print("-" * 60)
    resultado = buscar_cita(2)
    print(f"Retorno: {type(resultado).__name__} con ID {resultado['id'] if resultado else 'None'}")
    
    # TEST 5: Buscar otra cita existente
    print("\n📍 TEST 5: buscar_cita(1) - Buscar 'Dentista'")
    print("-" * 60)
    resultado = buscar_cita(1)
    
    # TEST 6: Buscar cita inexistente
    print("\n📍 TEST 6: buscar_cita(999) - Buscar cita que NO existe")
    print("-" * 60)
    resultado = buscar_cita(999)
    print(f"Retorno: {resultado}")
    
    # TEST 7: Eliminar cita (cuando esté implementado)
    # print("\n📍 TEST 7: eliminar_cita(3) - Eliminar 'Gimnasio'")
    # print("-" * 60)
    # eliminar_cita(3)
    # ver_citas()
    
    # RESUMEN FINAL
    print("\n" + "=" * 60)
    print("📊 RESUMEN FINAL")
    print("=" * 60)
    print(f"Total citas en memoria: {len(thdora_data['citas'])}")
    print(f"Funciones implementadas: 3/4")
    print(f"  ✅ agregar_cita()")
    print(f"  ✅ ver_citas()")
    print(f"  ✅ buscar_cita()")
    print(f"  ⏳ eliminar_cita() - Pendiente ejercicio 5")
    print("\n✅ Todos los tests completados correctamente")
    print("=" * 60)
