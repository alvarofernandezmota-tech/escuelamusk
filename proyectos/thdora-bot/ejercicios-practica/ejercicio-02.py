"""
THDORA - Ejercicio 2: agregar_cita()
Práctica personal

INSTRUCCIONES:
1. Lee primero: docs/ejercicios/02-agregar-cita.md
2. Escribe el código ABAJO (no copies, escribe tú)
3. Prueba: python ejercicios-practica/ejercicio-02.py
4. Si funciona Y lo entiendes → copia a src/thdora_functions.py

OBJETIVO:
Crear función agregar_cita() que añada citas al diccionario.

CONCEPTOS NUEVOS:
- Funciones con def
- Parámetros
- .append() para añadir a listas
- return para devolver valores
- IDs únicos

¡Ánimo! Tu primera función.
"""

# ==========================================
# IMPORTAR DATOS
# ==========================================

# TODO: Importar thdora_data desde el ejercicio 1
# Pista: from ejercicio_01 import thdora_data


# ==========================================
# FUNCIÓN agregar_cita
# ==========================================

def agregar_cita(nombre, fecha, hora_inicio, hora_fin, descripcion=''):
    """
    Añade una nueva cita al diccionario thdora_data
    
    Parámetros:
        nombre (str): Nombre de la cita (ej: 'Dentista')
        fecha (str): Fecha en formato YYYY-MM-DD (ej: '2026-02-10')
        hora_inicio (str): Hora inicio HH:MM (ej: '10:00')
        hora_fin (str): Hora fin HH:MM (ej: '11:00')
        descripcion (str): Descripción opcional (default: '')
    
    Returns:
        dict: La cita creada
    """
    
    # TODO: Crear diccionario nueva_cita con estos campos:
    # - 'id': número único (usa len(thdora_data['citas']) + 1)
    # - 'nombre': parámetro nombre
    # - 'fecha': parámetro fecha
    # - 'hora_inicio': parámetro hora_inicio
    # - 'hora_fin': parámetro hora_fin
    # - 'descripcion': parámetro descripcion
    
    
    # TODO: Añadir nueva_cita a thdora_data['citas']
    # Pista: usa .append()
    
    
    # TODO: Devolver nueva_cita
    # Pista: return nueva_cita
    
    pass  # Borra esto cuando escribas tu código


# ==========================================
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🧪 Testing agregar_cita()...\n")
    
    # TODO: Probar añadir 2-3 citas
    # Ejemplo:
    # cita1 = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    # print(f"✅ Cita 1: {cita1}")
    
    
    # TODO: Mostrar todas las citas
    # print(f"\n📊 Total citas: {len(thdora_data['citas'])}")
    # print(f"Todas las citas: {thdora_data['citas']}")
    
    pass