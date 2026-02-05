# 📚 Día 5 - Sesión 2: Machine Learning - Clustering K-Means

**Fecha:** 5 de febrero de 2026  
**Horario:** 19:00 - 21:00 (2 horas)  
**Tema:** Aprendizaje No Supervisado - K-Means en Profundidad

---

## 🎯 Objetivos de la Sesión

✅ Profundizar en clustering y sus aplicaciones  
✅ Dominar K-Means: convergencia y funcionamiento interno  
✅ Aprender métodos para elegir K óptimo  
✅ Comprender Elbow Method y Silhouette Coefficient  
✅ Explorar aplicaciones reales de aprendizaje no supervisado

---

## 📚 Contenido Cubierto

### 1. Clustering - Concepto Fundamental

**¿Qué resuelve?**
- Agrupa datos SIN etiquetas previas
- Encuentra patrones naturales automáticamente
- Maximiza similitud DENTRO de grupos
- Minimiza similitud ENTRE grupos

**Tipos de distancia:**
- **Euclidiana:** Línea recta entre puntos (la más común)
- **Manhattan:** Distancia en calles perpendiculares
- **Coseno:** Ángulo entre vectores (útil para texto)

### 2. K-Means - Algoritmo Detallado

**Proceso paso a paso:**
```
1. Elegir K (número de clusters)
2. Inicializar K centroides (aleatorios o K-Means++)
3. REPETIR hasta convergencia:
   a) ASIGNACIÓN: Cada punto al centroide más cercano
   b) ACTUALIZACIÓN: Recalcular centroides (promedio)
   c) VERIFICAR: ¿Centroides dejaron de moverse?
4. RETORNAR: Asignaciones y centroides finales
```

**Convergencia:**
- Se alcanza cuando centroides NO cambian
- O cuando cambio < tolerancia (ej: 0.0001)
- Típicamente: 10-50 iteraciones

**Implementación:**
- Desarrollamos versión manual desde cero (educativa)
- Comparamos con sklearn (validación)
- Visualizamos evolución iteración por iteración

### 3. Asignación de Clusters - Proceso de Predicción

**Regla fundamental:**
- Cada punto → centroide MÁS CERCANO
- Distancia euclidiana: `√Σ(xi - ci)²`

**Ejemplo paso a paso:**
```python
Punto P = [3, 3]
Centroides:
  C1 = [2, 2]  → distancia = 1.41
  C2 = [8, 8]  → distancia = 7.07
  C3 = [2, 8]  → distancia = 5.10

Mínima: 1.41 → Asignar a C1
```

**Confianza en asignación:**
- Alta: Muy cerca de su centroide, lejos de otros
- Baja: Distancias similares a múltiples centroides
- Punto en frontera: Equidistante

### 4. Elbow Method (Método del Codo)

**Concepto:**
- Prueba diferentes valores de K
- Calcula inercia (WCSS) para cada K
- Busca el "codo" en la curva

**Inercia (Within-Cluster Sum of Squares):**
- Suma de distancias² de cada punto a su centroide
- MENOR = mejor (clusters más compactos)
- Siempre decrece al aumentar K

**Interpretación:**
```
Antes del codo: Gran reducción de inercia
En el codo: Punto de equilibrio (K óptimo)
Después del codo: Poca mejora adicional
```

**Detección automática:**
- Segunda derivada (mayor cambio de pendiente)
- Método geométrico (distancia a línea referencia)

**Limitaciones:**
- A veces no hay codo claro
- Puede haber múltiples codos (ambiguo)
- Subjetivo (interpretación visual)

### 5. Silhouette Coefficient

**¿Qué mide?**
- Calidad de asignación de cada punto
- Combina cohesión (dentro) y separación (entre)

**Fórmula para punto i:**
```
a(i) = distancia promedio a su mismo cluster
b(i) = distancia promedio al cluster MÁS CERCANO

s(i) = (b(i) - a(i)) / max(a(i), b(i))
```

**Rango de valores:**
```
+1.0 : PERFECTO - Muy dentro de su cluster
+0.7 : EXCELENTE - Clusters bien definidos
+0.5 : BUENO - Estructura razonable
+0.25: ACEPTABLE - Estructura débil
 0.0 : FRONTERA - Entre clusters
-1.0 : MAL ASIGNADO - Debería estar en otro
```

**Silhouette Score global:**
- Promedio de todos los puntos
- Para elegir K: MAXIMIZAR este valor
- Más objetivo que Elbow Method

**Silhouette Diagram:**
- Visualiza silhouette de cada punto
- Por cluster y ordenado
- Identifica puntos mal asignados (negativos)

### 6. Comparación de Métodos

**Elbow Method:**
- ✅ Rápido, fácil de entender
- ❌ Subjetivo, a veces sin codo claro

**Silhouette Score:**
- ✅ Objetivo, mide cohesión + separación
- ✅ Identifica puntos mal asignados
- ❌ Más costoso computacionalmente

**Recomendación:**
- Usar AMBOS métodos
- Si coinciden → alta confianza
- Considerar conocimiento del dominio

---

## 🚀 Aplicaciones Reales del Aprendizaje No Supervisado

### 1. **Detección de Anomalías**

**Fraude bancario:**
- Patrón normal: Compras 20-100€, ciudad local, horario diurno
- Anomalía: 5000€, otro país, 3am, múltiples transacciones
- Algoritmo: Isolation Forest
- Impacto: 95% de fraudes detectados antes de completarse

**Mantenimiento predictivo:**
- Sensores en maquinaria (temperatura, vibración, presión)
- Detectar comportamiento anómalo ANTES del fallo
- Impacto: 70% reducción en paradas no planificadas

**Ciberseguridad:**
- Detectar ataques DDoS en tiempo real
- Tráfico anómalo vs patrón normal
- Bloqueo automático de amenazas

### 2. **Sistemas de Recomendación**

**Filtrado colaborativo:**
- Netflix, Spotify, Amazon
- Agrupa usuarios con gustos similares
- "Si te gustó X, también te gustará Y"
- Impacto: 80% del contenido consumido en Netflix

**Market Basket Analysis:**
- "Los clientes que compran X también compran Y"
- Optimización de disposición de productos

### 3. **Segmentación de Clientes**

**E-commerce:**
- Agrupa clientes sin categorías predefinidas
- Descubre segmentos: VIPs, Leales, Ocasionales, Dormidos
- Campañas de marketing personalizadas
- Impacto: +30% en conversión

**Resultados típicos:**
- 5% VIPs → 40% ingresos (atención premium)
- 25% Leales → 35% ingresos (fidelización)
- 50% Ocasionales → 20% ingresos (activación)
- 20% Dormidos → 5% ingresos (reactivación/descarte)

### 4. **Procesamiento de Imágenes**

**Medicina:**
- Segmentación de radiografías (tejidos, tumores)
- Detección temprana de cáncer
- Clustering de intensidades de píxeles

**Compresión:**
- Reducir colores: 16 millones → 16 colores dominantes
- Tamaño: 90% menor, calidad: ~95% similar

### 5. **Procesamiento de Lenguaje Natural**

**Organización de documentos:**
- Agrupa miles de documentos automáticamente
- Google News: agrupa noticias similares
- Topic Modeling (LDA): Descubre temas ocultos

### 6. **Medicina y Salud**

**Descubrimiento de subtipos:**
- 5 subtipos de diabetes descubiertos con clustering (2018)
- Tratamientos personalizados por subtipo
- Mejora en eficacia de medicamentos

### 7. **Otras Aplicaciones**

- 🎵 **Spotify:** Generación de playlists (Discover Weekly)
- 🏙️ **Urbanismo:** Planificación de transporte público
- 🧬 **Genética:** Agrupar genes con funciones similares
- 🌡️ **Clima:** Descubrir patrones climáticos no conocidos

---

## 💡 Conexión con Python y Proyectos Personales

### ML + Python = Superpoder

**Para THDORA (tu proyecto de hábitos):**

1. **Clustering:**
   - Agrupar días similares automáticamente
   - "Lunes y martes son parecidos, viernes es diferente"

2. **Detección de anomalías:**
   - Identificar días "raros" automáticamente
   - "Hoy tu patrón es muy diferente, ¿todo bien?"

3. **Pattern Discovery:**
   - Descubrir relaciones ocultas
   - "Cuando duermes poco + no desayunas → baja productividad"
   - Sin que tú le digas explícitamente qué buscar

4. **Predicción:**
   - Predecir productividad según hora/día
   - Recomendar mejor momento para cada tarea
   - Estimar duración real de tareas

**Ventajas del ML:**
- ✅ NO necesitas etiquetar datos manualmente
- ✅ Descubre patrones OCULTOS
- ✅ Escalable a millones de datos
- ✅ Se adapta con nuevos datos
- ✅ Automatización inteligente

---

## 🔧 Herramientas y Código

### Librerías principales:
```python
scikit-learn  # K-Means, métricas, preprocesamiento
numpy         # Operaciones numéricas
pandas        # Manejo de datos
matplotlib    # Visualización
```

### Implementaciones desarrolladas:
1. ✅ K-Means manual desde cero (educativo)
2. ✅ Cálculo de inercia paso a paso
3. ✅ Silhouette manual con explicaciones
4. ✅ Elbow Method con detección automática de codo
5. ✅ Silhouette Diagram completo
6. ✅ Comparación visual de métodos
7. ✅ Visualización de convergencia iterativa

---

## 📊 Conceptos Clave Aprendidos

### K-Means:
- Algoritmo iterativo hasta convergencia
- Asignación basada en distancia mínima
- Sensible a inicialización (usar K-Means++)
- Mini-Batch K-Means para datasets grandes

### Evaluación de Clustering:
- **Inercia (WCSS):** Compacidad de clusters (menor mejor)
- **Silhouette Score:** Calidad de asignación [-1, +1] (mayor mejor)
- **Davies-Bouldin Index:** Separación entre clusters (menor mejor)
- **Calinski-Harabasz:** Ratio varianza inter/intra (mayor mejor)

### Elegir K óptimo:
1. Elbow Method → Buscar "codo" visual
2. Silhouette Score → Maximizar
3. Davies-Bouldin → Minimizar
4. Combinar múltiples métricas
5. Considerar conocimiento del dominio

---

## 🎯 Plan de Implementación Futura

### Para sistema de hábitos/horarios con ML:

**Fase 1: Recolección (Mes 1)**
- Registrar todas las sesiones/tareas
- Mínimo 60 registros antes de entrenar
- Solo acumular datos, sin ML

**Fase 2: Primeros Modelos (Mes 2)**
- Entrenar modelo de clustering (patrones de días)
- Modelo de predicción de productividad
- Validar con métricas

**Fase 3: Refinamiento (Mes 3+)**
- Re-entrenar con más datos
- Ajustar hiperparámetros
- Optimización automática de horarios

**Datos a recolectar:**
```python
{
    "fecha": "2026-02-05",
    "hora_inicio": 10,
    "dia_semana": 3,
    "tipo_tarea": "estudiar",
    "duracion_planificada": 120,
    "horas_sueno_previas": 7,
    "energia_inicial": 7,
    "completada": True,
    "duracion_real": 135,
    "productividad": 8
}
```

---

## 📝 Próximos Pasos

1. ✅ Documentar toda la sesión (este archivo)
2. ⏳ Actualizar apuntes en repo personal
3. ⏳ Sesión THDORA (1 hora) - Aplicar conceptos aprendidos
4. ⏳ Implementar sistema de registro básico para acumular datos

---

## 🎓 Reflexión

**Lo más importante de hoy:**
- Machine Learning NO supervisado es increíblemente poderoso
- No necesita datos etiquetados (CARO de obtener)
- Clustering encuentra patrones que humanos no ven
- Aplicaciones en TODOS los campos: finanzas, salud, marketing, etc.
- Python + ML = Diferenciación profesional masiva

**Siguiente objetivo:**
- Aplicar estos conceptos a THDORA
- Empezar a recolectar datos estructurados
- En 30 días: primer modelo entrenado

---

## ⏰ Registro de Tiempo

- **19:00 - 19:30:** Clustering general y K-Means fundamentals
- **19:30 - 20:00:** Convergencia, asignación, predicción
- **20:00 - 20:30:** Elbow Method y elegir K óptimo
- **20:30 - 20:45:** Silhouette Coefficient profundo
- **20:45 - 21:00:** Aplicaciones reales ML no supervisado

**Duración total:** 2 horas  
**Intensidad:** Alta - Muchos conceptos nuevos  
**Comprensión:** 85% - Necesito practicar implementaciones

---

## 📚 Recursos para Revisar

- Implementaciones manuales de algoritmos
- Visualizaciones de convergencia
- Ejemplos de aplicaciones reales
- Código de detección de anomalías
- Plan de implementación THDORA con ML

---

**Estado:** ✅ Sesión completada  
**Siguiente:** 🚀 1 hora THDORA - Aplicar conceptos

---

*Generado el 5 de febrero de 2026 a las 21:00*