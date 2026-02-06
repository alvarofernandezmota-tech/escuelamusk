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

# Ejemplo de cita (estructura que usaremos):
# {
#     'id': 1,
#     'titulo': 'Dentista',
#     'fecha': '2026-02-10',
#     'hora': '10:00',
#     'descripcion': 'Revisión anual'
# }


# ==========================================
# ZONA DE PRUEBAS
# ==========================================
if __name__ == "__main__":
    print("🤖 THDORA v0.1 - Diccionario base\n")
    
    print("Diccionario inicial:")
    print(thdora_data)
    print(f"\nNúmero de citas: {len(thdora_data['citas'])}")
    print("\n✅ Diccionario creado correctamente")