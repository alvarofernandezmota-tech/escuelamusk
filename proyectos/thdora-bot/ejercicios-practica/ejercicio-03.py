"""
THDORA - Ejercicio 3: ver_citas()
Práctica personal

INSTRUCCIONES:
1. Lee primero: docs/ejercicios/03-ver-citas.md
2. Escribe el código ABAJO (no copies, escribe tú)
3. Prueba: python ejercicios-practica/ejercicio-03.py
4. Si funciona Y lo entiendes → copia función a src/thdora_functions.py

OBJETIVO:
Crear función ver_citas() que muestre todas las citas o mensaje si no hay.

¡Ánimo! Ya dominas agregar_cita(), ahora a visualizar.
"""

# ==========================================
# DATOS (temporal para testing)
# ==========================================
thdora_data = {
    'citas': []
}


# ==========================================
# FUNCIÓN agregar_cita (para testing)
# ==========================================
def agregar_cita(nombre, fecha, hora_inicio, hora_fin):
    """Añade una nueva cita (para poder probar ver_citas)"""
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
# ESCRIBE TU CÓDIGO AQUÍ ↓
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
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🧪 Testing ver_citas()...\n")
    
    # Caso 1: Sin citas
    print("=" * 50)
    print("Caso 1: Lista vacía")
    print("=" * 50)
    ver_citas()
    
    print("\n" + "=" * 50)
    print("Caso 2: Con citas añadidas")
    print("=" * 50)
    
    # Añadir citas de prueba
    agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    agregar_cita("Reunión equipo", "2026-02-12", "09:00", "10:30")
    agregar_cita("Gimnasio", "2026-02-13", "18:00", "19:00")
    
    # Mostrar todas las citas
    ver_citas()
    
    print("\n✅ Testing completado")
