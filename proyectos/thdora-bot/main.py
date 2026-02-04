"""
THDORA Bot - Bot de gestión de agenda personal
Autor: Álvaro Fernández Mota
Versión: 0.1.0
Fecha: 2026-02-04
"""

# Importará las funciones cuando las creemos
# from funciones.agregar_cita import agregar_cita
# from funciones.mostrar_citas import mostrar_citas_dia, mostrar_citas_mes
# from funciones.eliminar_cita import eliminar_cita
# from funciones.buscar_cita import buscar_cita
# from funciones.guardar_datos import cargar_datos, guardar_datos
import json


def mostrar_menu():
    """
    Muestra el menú principal de THDORA
    """
    print("\n" + "="*50)
    print(" " * 15 + "THDORA BOT 📅")
    print(" " * 10 + "Gestión de Agenda Personal")
    print("="*50)
    print("\n1. Agregar cita")
    print("2. Ver citas del día")
    print("3. Ver citas del mes")
    print("4. Eliminar cita")
    print("5. Buscar cita")
    print("6. Salir")
    print("\n" + "-"*50)


def saludar_usuario():
    """
    Carga el usuario y muestra saludo personalizado.
    Devuelve el nombre del usuario.
    """
    with open("datos/usuario.json", "r", encoding="utf-8") as file:
        usuario = json.load(file)
    
    nombre_usuario = usuario["nombre"]
    
    print("\n" + "="*50)
    print(f"👋 ¡Hola {nombre_usuario}! Bienvenido a THDORA")
    print("🗓️  Tu asistente de agenda personal")
    print("="*50)
    
    return nombre_usuario


def main():
    """
    Función principal del bot
    """
    # Diccionario en memoria para las citas (luego lo cargaremos de JSON)
    agenda = {}
    
    # Saludo personalizado al iniciar
    nombre_usuario = saludar_usuario()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()
        
        if opcion == "1":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a agregar_cita(agenda)
            
        elif opcion == "2":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a mostrar_citas_dia(agenda)
            
        elif opcion == "3":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a mostrar_citas_mes(agenda)
            
        elif opcion == "4":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a eliminar_cita(agenda)
            
        elif opcion == "5":
            print("\n[FUNCIONALIDAD EN DESARROLLO]")
            # Aquí llamaremos a buscar_cita(agenda)
            
        elif opcion == "6":
            print(f"\n👋 Hasta pronto, {nombre_usuario}! Tus citas están guardadas.")
            # Aquí llamaremos a guardar_datos(agenda)
            break
            
        else:
            print("\n❌ Opción inválida. Por favor, elige del 1 al 6.")


if __name__ == "__main__":
    main()
