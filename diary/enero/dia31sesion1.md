# Día 31 de enero - Sesión 1: Tuplas (Ejercicios 1-8)

## 📅 Fecha
31 de enero de 2026 - 20:17 CET

## 🎯 Tema
Tuplas - Ejercicios prácticos y ordenación

## ✅ Ejercicios completados
1. Crear tupla con 5 elementos
2. Acceder a elementos (primero y último)
3. Slice de tupla
4. Concatenar dos tuplas
5. Repetir tupla
6. Verificar existencia de elemento
7. Métodos count() e index()
8. **Ordenar tupla de tuplas por 2º elemento** (concepto clave: `lambda x: x[índice]`)

## 🔑 Conceptos clave aprendidos
- **Ordenación de tuplas de tuplas:** `lista.sort(key=lambda x: x[1])`
- El índice `[0]`, `[1]`, `[2]`... indica **por qué posición ordenar**
- `x[0]` → ordena por 1º elemento
- `x[1]` → ordena por 2º elemento  
- `x[2]` → ordena por 3º elemento
- Siempre el mismo patrón: convertir a lista → ordenar → convertir a tupla

## 📊 Progreso
- **Módulo 2 - Fundamentos:** Tuplas (8/9 ejercicios)
- Próximo: Ejercicio 9 y diccionarios

## 💡 Notas importantes
- Las tuplas son **inmutables**, por eso hay que convertir a lista para ordenar
- La separación inicial en tuplas de tuplas NO es obligatoria si ya viene así desde el principio
- Fórmula mágica: `list()` → `.sort(key=lambda x: x[índice])` → `tuple()`

## 🐕 Interrupciones
- Perra pidiendo salir (finalización anticipada)
- Continuaremos con diccionarios en la próxima sesión
