"""
THDORA - Ejercicio 1: Diccionario Base
Práctica personal

INSTRUCCIONES:
1. Lee primero: docs/ejercicios/01-diccionario-base.md
2. Escribe el código ABAJO (no copies, escribe tú)
3. Prueba: python ejercicios-practica/ejercicio-01.py
4. Si funciona Y lo entiendes → copia a src/thdora_data.py

OBJETIVO:
Crear un diccionario llamado 'thdora_data' con una lista vacía de citas.

¡Ánimo! Es tu primer ejercicio Python aplicado.
"""

# ==========================================
# ESCRIBE TU CÓDIGO AQUÍ ↓
# ==========================================

# Crear diccionario thdora_data
thdora_data = {
    'citas': []
}

# ==========================================
# ZONA DE TESTING
# ==========================================

if __name__ == "__main__":
    print("🤖 THDORA v0.1 - Diccionario base\n")
    print("Diccionario inicial:")
    print(thdora_data)
    print(f"\nNúmero de citas: {len(thdora_data['citas'])}")
    print("\n✅ Diccionario creado correctamente")
