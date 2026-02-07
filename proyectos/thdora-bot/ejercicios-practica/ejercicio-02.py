"""
THDORA - Funciones de citas
Fecha: 06 febrero 2026
Autor: Álvaro Fernández Mota
"""

# ==========================================
# IMPORTS
# ==========================================


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
# TESTING
# ==========================================
if __name__ == "__main__":
    print("🧪 Testing agregar_cita()...\n")
    
    cita1 = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    print(f"✅ Cita 1: {cita1}")
    
    cita2 = agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00")
    print(f"✅ Cita 2: {cita2}")
    
    print(f"\n📊 Total citas: {len(thdora_data['citas'])}")
