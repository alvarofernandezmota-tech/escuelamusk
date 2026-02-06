"""
THDORA v0.1 - Bot de gestión de citas
Fecha: 6 febrero 2026
Autor: Álvaro Fernández Mota

VERSION 0.1: Diccionario MÍNIMO
- Solo citas
- Sin categorías (después)
- Sin usuario (después)
- Sin JSON (después)

Este es el PUNTO DE PARTIDA.
Irá creciendo ejercicio por ejercicio.
"""

# ==========================================
# DICCIONARIO BASE
# ==========================================

thdora_data = {
    'citas': []  # Lista vacía de citas
}

# ==========================================
# ESTRUCTURA DE UNA CITA (para más adelante)
# ==========================================
"""
Cuando agregemos citas (Ejercicio 2), tendrán esta estructura:

{
    'id': 1,                        # Número único
    'nombre': 'Dentista',           # Nombre de LA CITA (no del usuario)
    'fecha': '2026-02-10',          # Formato: YYYY-MM-DD
    'hora_inicio': '10:00',         # Formato: HH:MM
    'hora_fin': '11:00',            # Formato: HH:MM
    'descripcion': 'Revisión anual' # Opcional
}

IMPORTANTE:
- 'nombre' = nombre de LA CITA (ej: "Dentista", "Reunión", "Comida")
- 'hora_inicio' y 'hora_fin' = rango completo de tiempo
- Más adelante: categoría, prioridad, completada, etc.
"""


# ==========================================
# ZONA DE PRUEBAS
# ==========================================
if __name__ == "__main__":
    print("🤖 THDORA v0.1 - Diccionario base\n")
    
    print("Diccionario inicial:")
    print(thdora_data)
    print(f"\nNúmero de citas: {len(thdora_data['citas'])}")
    print("\n✅ Diccionario creado correctamente")
    print("\n➡️  Siguiente: Ejercicio 2 - agregar_cita()")