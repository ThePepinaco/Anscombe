# Universidad Politécnica Salesiana (UPS)
## Carrera de Computación
### Período 2024-2024
### Estudiante: Santiago Torres

---

## Introducción Teórica al Cuarteto de Anscombe

El Cuarteto de Anscombe es un conjunto de cuatro datasets creados por el estadístico Francis Anscombe en 1973 para demostrar la importancia de visualizar datos antes de analizarlos estadísticamente. Aunque estos cuatro datasets tienen estadísticas descriptivas casi idénticas (media, varianza, correlación, y coeficiente de regresión lineal), sus gráficos revelan patrones muy diferentes. Esto destaca la necesidad de visualizar los datos para evitar conclusiones erróneas basadas únicamente en estadísticas numéricas.

### Ejemplos de Visualización

![Cuarteto de Anscombe](https://upload.wikimedia.org/wikipedia/commons/e/ec/Anscombe%27s_quartet_3.svg)

**Figura 1:** Visualización de los cuatro conjuntos de datos del Cuarteto de Anscombe. Cada gráfico muestra una dispersión diferente de datos, a pesar de tener estadísticas descriptivas similares.

### Referencias

- Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17-21.
- [Wikipedia: Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)

---

## Estructura del Proyecto

### Directorio `data`

Este directorio contiene todos los conjuntos de datos utilizados para la práctica, incluyendo el Cuarteto de Anscombe y otros datasets utilizados para análisis y visualización.

### Directorio `R`

En este directorio se guarda el código R utilizado para visualizar y analizar los datasets. Se incluyen scripts específicos para cada uno de los 13 conjuntos de datos.

### Directorio `PYTHON`

Guarda el código y los resultados de la regresión lineal aplicada a uno de los datasets del Datasaurus.

#### Código de Regresión Lineal en Python

El script `regresion_lineal.py` realiza una regresión lineal, cuadrática y cúbica en el subconjunto "bullseye" del dataset `datasaurus.csv`. A continuación se detalla brevemente cada sección del código:

1. **Importación de Librerías:**
   - Se importan las librerías necesarias: `pandas`, `sklearn`, `matplotlib`, `numpy`, y `os`.

2. **Carga del Dataset:**
   - Se carga el archivo `datasaurus.csv` y se filtra el subconjunto "bullseye".

3. **Preparación de los Datos:**
   - Se preparan las variables `X` (independiente) e `y` (dependiente) para el análisis.

4. **Creación y Entrenamiento de Modelos:**
   - Se crean y entrenan modelos de regresión lineal, cuadrática y cúbica usando `LinearRegression` y `PolynomialFeatures`.

5. **Predicciones:**
   - Se calculan las predicciones para cada modelo a lo largo de un rango de valores de `X`.

6. **Visualización:**
   - Se grafican los datos originales y las líneas de regresión para cada modelo.


---