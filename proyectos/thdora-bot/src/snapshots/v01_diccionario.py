"""
THDORA - Snapshot v01
Fecha: 6 febrero 2026
Estado: DESPUÉS de completar Ejercicio 1

FUNCIONES INCLUIDAS:
(ninguna todavía)

PENDIENTES:
⏳ agregar_cita()
⏳ ver_citas()
⏳ buscar_cita()
⏳ eliminar_cita()
⏳ modificar_cita()
⏳ guardar_json()
⏳ cargar_json()
"""

# ==========================================
# DICCIONARIO BASE
# ==========================================

thdora_data = {
    'citas': []  # Lista vacía de citas
}

# Ejemplo de cita (estructura):
# {
#     'id': 1,
#     'titulo': 'Dentista',
#     'fecha': '2026-02-10',
#     'hora': '10:00',
#     'descripcion': 'Revisión anual'
# }


if __name__ == "__main__":
    print("🤖 THDORA v0.1 Snapshot\n")
    print(thdora_data)
    print(f"\nCitas: {len(thdora_data['citas'])}")