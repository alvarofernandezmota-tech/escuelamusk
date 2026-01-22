colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
print(colores[1:-1])  # Imprime todos los colores excepto el primero y el último
print(len(colores))  # Imprime la longitud de la lista
print("----------------------")  # Imprime una línea de separación
colores[0] = "rosa"  # Cambia el primer color a "rosa"
print(colores)  # Imprime la lista actualizada
colores.append("morado")  # Añade "morado" al final de la lista
print(colores)  # Imprime la lista actualizada
ordernado = sorted(colores)  # Crea una nueva lista ordenada
print(ordernado)  # Imprime la lista ordenada
print(colores)  # Imprime la lista original sin cambios
colores.remove("verde")  # Elimina "verde" de la lista
colores[0] = "morado"
print(colores)  # Imprime la lista actualizada
print("----------------------")  # Imprime una línea de separación
existe = "verde" in colores  # Verifica si "verde" está en la lista
print(existe)    # Imprime el resultado de la verificación
print("----------------------")  # Imprime una línea de separación
