"""
THDORA - Ejercicio 2: agregar_cita()
Práctica personal - COMPLETADO ✅

OBJETIVO:
Crear función agregar_cita() que añada citas al diccionario.

CONCEPTOS PRACTICADOS:
- Funciones con def
- Parámetros (nombre, fecha, hora_inicio, hora_fin)
- .append() para añadir a listas
- return para devolver valores
- IDs únicos con len()
"""

# ==========================================
# DATOS (temporal para testing)
# ==========================================
thdora_data = {
    'citas': []
}


# ==========================================
# FUNCIÓN agregar_cita
# ==========================================

def agregar_cita(nombre, fecha, hora_inicio, hora_fin):
    """
    Añade una nueva cita al diccionario thdora_data
    
    Parámetros:
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