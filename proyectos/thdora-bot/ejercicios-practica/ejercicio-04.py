"""
THDORA - Ejercicio 4: buscar_cita()
Práctica personal

INSTRUCCIONES:
1. Lee primero: docs/ejercicios/04-buscar-cita.md
2. Escribe el código ABAJO (no copies, escribe tú)
3. Prueba: python ejercicios-practica/ejercicio-04.py
4. Si funciona Y lo entiendes → añade a src/thdora_functions.py

OBJETIVO:
Crear función buscar_cita() que encuentre citas por nombre.

CONCEPTOS NUEVOS:
- Búsqueda en listas
- Comparación de strings
- return None cuando no encuentra
- .lower() para búsqueda case-insensitive

¡Ánimo!
"""

# ==========================================
# IMPORTAR DATOS Y FUNCIONES
# ==========================================

# TODO: Importar thdora_data
# TODO: Importar agregar_cita (para testing)


# ==========================================
# FUNCIÓN buscar_cita
# ==========================================

def buscar_cita(nombre_buscar):
    """
    Busca citas por nombre (búsqueda parcial, case-insensitive)
    
    Parámetros:
        nombre_buscar (str): Texto a buscar en el nombre de las citas
    
    Returns:
        list: Lista de citas que coinciden (puede estar vacía)
    """
    
    # TODO: Crear lista vacía para resultados
    # resultados = []
    
    
    # TODO: Convertir nombre_buscar a minúsculas
    # nombre_lower = nombre_buscar.lower()
    
    
    # TODO: Recorrer todas las citas
    # for cita in thdora_data['citas']:
    #     Si nombre_lower está en cita['nombre'].lower():
    #         Añadir cita a resultados
    
    
    # TODO: Devolver lista de resultados
    # return resultados
    
    pass  # Borra esto cuando escribas tu código


# ==========================================
# FUNCIÓN buscar_cita_por_id (BONUS)
# ==========================================

def buscar_cita_por_id(id_cita):
    """
    Busca una cita específica por su ID
    
    Parámetros:
        id_cita (int): ID de la cita a buscar
    
    Returns:
        dict: La cita encontrada, o None si no existe
    """
    for cita in thdora_data['citas']:
        if cita['id'] == id_cita:
            print(f"\n CITA ENCOONTRADA:")
            print(f"[{cita['id']}]{cita['nombre']}")
            print(                {cita['fecha']})
            print(f" Hora inicio: {cita['hora inicio']}")
            print(f" Hora final: {cita['hora_fin']} ")
            return
    print(f"Cita con ID {id_cita} no encontrada")
    # TODO: Recorrer todas las citas
    # for cita in thdora_data['citas']:
    #     Si cita['id'] == id_cita:
    #         return cita
    
    
    # TODO: Si no encuentra nada, devolver None
    # return None
    
    pass  # Borra esto cuando escribas tu código


# ==========================================
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🧪 Testing buscar_cita()...\n")
    
    # TODO: Añadir citas de prueba
    # agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    # agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    # agregar_cita("Estudiar JavaScript", "2026-02-12", "16:00", "18:00")
    # agregar_cita("Reunión", "2026-02-13", "09:00", "10:00")
    
    
    # TODO: Probar búsqueda por nombre
    # print("Buscando 'estudiar':")
    # resultados = buscar_cita("estudiar")
    # print(f"Encontradas: {len(resultados)} citas")
    # for cita in resultados:
    #     print(f"  - {cita['nombre']}")
    
    
    # TODO: Probar búsqueda por ID
    # print("\nBuscando cita ID=2:")
    # cita = buscar_cita_por_id(2)
    # if cita:
    #     print(f"✅ Encontrada: {cita['nombre']}")
    # else:
    #     print("❌ No encontrada")
    
"""
THDORA - Ejercicio 4: buscar_cita_por_id()
Práctica personal - COMPLETADO ✅
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
    """Añade una nueva cita"""
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
# FUNCIÓN buscar_cita_por_id
# ==========================================

def buscar_cita_por_id(id_cita):
    """
    Busca una cita específica por su ID
    
    Parámetros:
        id_cita (int): ID de la cita a buscar
    
    Returns:
        dict: La cita encontrada, o None si no existe
    """
    for cita in thdora_data['citas']:
        if cita['id'] == id_cita:
            print(f"\n📌 CITA ENCONTRADA:")
            print(f"[{cita['id']}] {cita['nombre']}")
            print(f"    📅 {cita['fecha']}")
            print(f"    ⏰ {cita['hora_inicio']} - {cita['hora_fin']}")
            return cita
    
    print(f"❌ Cita con ID {id_cita} no encontrada")
    return None


# ==========================================
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🧪 Testing buscar_cita_por_id()...\n")
    
    # Añadir citas de prueba
    agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    agregar_cita("Reunión equipo", "2026-02-12", "09:00", "10:30")
    
    print("=" * 50)
    print("Caso 1: Buscar cita que existe (ID=1)")
    print("=" * 50)
    cita = buscar_cita_por_id(1)
    
    print("\n" + "=" * 50)
    print("Caso 2: Buscar cita que NO existe (ID=999)")
    print("=" * 50)
    cita = buscar_cita_por_id(999)
    
    print("\n✅ Testing completado - Ejercicio 4 funcional")
