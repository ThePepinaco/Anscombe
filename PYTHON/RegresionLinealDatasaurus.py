import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np
import os
# Cargar el conjunto de datos desde el archivo CSV
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, '..', 'directorio', 'datasaurus.csv')

data = pd.read_csv(file_path)

# Filtrar los datos solo para el grupo "bullseye"
bullseye_data = data[data['dataset'] == 'bullseye']

# Supongamos que las columnas son 'x' y 'y', ajusta si es necesario
X = bullseye_data['x'].values.reshape(-1, 1)  # Feature (variable independiente)
y = bullseye_data['y'].values                  # Target (variable dependiente)

# Crear el modelo de regresión lineal
linear_model = LinearRegression()
linear_model.fit(X, y)

# Crear el modelo de regresión cuadrática
quadratic_features = PolynomialFeatures(degree=2)
X_quad = quadratic_features.fit_transform(X)
quadratic_model = LinearRegression()
quadratic_model.fit(X_quad, y)

# Crear el modelo de regresión polinomial de grado 3
cubic_features = PolynomialFeatures(degree=3)
X_cubic = cubic_features.fit_transform(X)
cubic_model = LinearRegression()
cubic_model.fit(X_cubic, y)

# Calcular las predicciones para todos los modelos
X_fit = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_fit_quad = quadratic_features.transform(X_fit)
X_fit_cubic = cubic_features.transform(X_fit)
linear_predictions = linear_model.predict(X_fit)
quadratic_predictions = quadratic_model.predict(X_fit_quad)
cubic_predictions = cubic_model.predict(X_fit_cubic)

# Graficar los datos y las líneas de regresión
plt.scatter(X, y, label='Datos')
plt.plot(X_fit, linear_predictions, color='red', label='Regresión Lineal')
plt.plot(X_fit, quadratic_predictions, color='green', label='Regresión Cuadrática')
plt.plot(X_fit, cubic_predictions, color='blue', label='Regresión Cúbica')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal, Cuadrática y Cúbica para el Grupo "Bullseye"')
plt.legend()
plt.grid(True)
plt.show()
