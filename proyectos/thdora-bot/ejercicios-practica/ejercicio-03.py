"""
THDORA - Ejercicio 3: ver_citas()
Práctica personal

INSTRUCCIONES:
1. Lee primero: docs/ejercicios/03-ver-citas.md
2. Escribe el código ABAJO (no copies, escribe tú)
3. Prueba: python ejercicios-practica/ejercicio-03.py
4. Si funciona Y lo entiendes → añade a src/thdora_functions.py

OBJETIVO:
Crear función ver_citas() que muestre todas las citas formateadas.

CONCEPTOS NUEVOS:
- Bucle for para recorrer listas
- if/else para condicionales
- f-strings para formateo
- Función sin return (solo muestra)

¡Ánimo!
"""

# ==========================================
# IMPORTAR DATOS Y FUNCIONES
# ==========================================

# TODO: Importar thdora_data
# TODO: Importar agregar_cita (para testing)


# ==========================================
# FUNCIÓN ver_citas
# ==========================================

def ver_citas():
    """
    Muestra todas las citas del diccionario thdora_data
    de forma formateada y legible.
    
    No devuelve nada, solo imprime en consola.
    """
    
    # TODO: Verificar si hay citas
    # Si len(thdora_data['citas']) == 0:
    #     print("📭 No hay citas registradas")
    #     return
    
    
    # TODO: Mostrar encabezado
    # print(f"\n📅 CITAS REGISTRADAS ({len(thdora_data['citas'])})\n")
    # print("=" * 50)
    
    
    # TODO: Recorrer todas las citas con for
    # for cita in thdora_data['citas']:
    #     Mostrar cada cita formateada
    #     Ejemplo: print(f"[{cita['id']}] {cita['nombre']}")
    #              print(f"    📅 {cita['fecha']} | ⏰ {cita['hora_inicio']}-{cita['hora_fin']}")
    #              if cita['descripcion']:
    #                  print(f"    📝 {cita['descripcion']}")
    #              print()  # Línea en blanco
    
    pass  # Borra esto cuando escribas tu código


# ==========================================
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🧪 Testing ver_citas()...\n")
    
    # TODO: Añadir algunas citas de prueba
    # agregar_cita("Dentista", "2026-02-10", "10:00", "11:00", "Revisión anual")
    # agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    # agregar_cita("Reunión equipo", "2026-02-12", "09:00", "10:30", "Proyecto THDORA")
    
    
    # TODO: Probar ver_citas()
    # ver_citas()
    
    pass