"""
THDORA - Ejercicio 5: eliminar_cita()
Práctica personal

INSTRUCCIONES:
1. Lee primero: docs/ejercicios/05-eliminar-cita.md
2. Escribe el código ABAJO (no copies, escribe tú)
3. Prueba: python ejercicios-practica/ejercicio-05.py
4. Si funciona Y lo entiendes → añade a src/thdora_functions.py

OBJETIVO:
Crear función eliminar_cita() que borre citas por ID.

CONCEPTOS NUEVOS:
- Eliminar elementos de lista
- enumerate() para índice + elemento
- .pop() para eliminar por índice
- return True/False para indicar éxito

¡Ánimo! Último ejercicio de fundamentos.
"""

# ==========================================
# IMPORTAR DATOS Y FUNCIONES
# ==========================================

# TODO: Importar thdora_data
# TODO: Importar agregar_cita, ver_citas (para testing)


# ==========================================
# FUNCIÓN eliminar_cita
# ==========================================

def eliminar_cita(id_cita):
    """
    Elimina una cita por su ID
    
    Parámetros:
        id_cita (int): ID de la cita a eliminar
    
    Returns:
        bool: True si se eliminó, False si no se encontró
    """
    
    # TODO: Buscar la cita por ID usando enumerate
    # for indice, cita in enumerate(thdora_data['citas']):
    #     Si cita['id'] == id_cita:
    #         Eliminar cita usando .pop(indice)
    #         return True
    
    
    # TODO: Si no se encontró, devolver False
    # return False
    
    pass  # Borra esto cuando escribas tu código


# ==========================================
# FUNCIÓN eliminar_todas_citas (BONUS)
# ==========================================

def eliminar_todas_citas():
    """
    Elimina TODAS las citas del diccionario
    
    Returns:
        int: Número de citas eliminadas
    """
    
    # TODO: Contar cuántas citas hay
    # cantidad = len(thdora_data['citas'])
    
    
    # TODO: Vaciar la lista
    # thdora_data['citas'] = []
    
    
    # TODO: Devolver cantidad eliminada
    # return cantidad
    
    pass  # Borra esto cuando escribas tu código


# ==========================================
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🧪 Testing eliminar_cita()...\n")
    
    # TODO: Añadir citas de prueba
    # agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    # agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00")
    # agregar_cita("Reunión", "2026-02-12", "09:00", "10:00")
    
    
    # TODO: Mostrar citas antes de eliminar
    # print("📅 Citas antes de eliminar:")
    # ver_citas()
    
    
    # TODO: Eliminar cita ID=2
    # print("\n🗑️  Eliminando cita ID=2...")
    # if eliminar_cita(2):
    #     print("✅ Cita eliminada")
    # else:
    #     print("❌ Cita no encontrada")
    
    
    # TODO: Mostrar citas después de eliminar
    # print("\n📅 Citas después de eliminar:")
    # ver_citas()
    
    
    # TODO: Probar eliminar cita inexistente
    # print("\n🗑️  Intentando eliminar cita ID=999...")
    # if eliminar_cita(999):
    #     print("✅ Eliminada")
    # else:
    #     print("❌ No existe esa cita")
    
    pass