"""
THDORA - Funciones de citas
Fecha: 06 febrero 2026
Autor: Álvaro Fernández Mota
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
# TESTING
# ==========================================
if __name__ == "__main__":
    print("🧪 Testing funciones THDORA...\n")
    
    # Test 1: Ver citas vacío
    print("=== TEST 1: ver_citas() sin citas ===")
    ver_citas()
    
    print("\n" + "=" * 50 + "\n")
    
    # Test 2: Agregar citas
    print("=== TEST 2: agregar_cita() ===")
    cita1 = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    print(f"✅ Cita 1: {cita1}")
    
    cita2 = agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00")
    print(f"✅ Cita 2: {cita2}")
    
    cita3 = agregar_cita("Reunión", "2026-02-12", "09:00", "10:30")
    print(f"✅ Cita 3: {cita3}")
    
    print("\n" + "=" * 50 + "\n")
    
    # Test 3: Ver todas las citas
    print("=== TEST 3: ver_citas() con 3 citas ===")
    ver_citas()
    
    print(f"📊 Total citas en memoria: {len(thdora_data['citas'])}")
    print("\n✅ Testing completado")
