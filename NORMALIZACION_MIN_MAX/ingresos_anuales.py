# -*- coding: utf-8 -*-
# Normalización Min-Max - Ingresos Anuales
# Normalización simple de edad e ingresos

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Datos de empleados
datos = {
    'Empleado': ['Andrea', 'Blanca Inés', 'Carla María', 'Viviana Montoya', 'Juan Pérez', 'Iván Cepeda'],
    'Edad': [15, 32, 25, 22, 41, 20],
    'Ingreso': [800, 1000, 1200, 5000, 1500, 3500]
}

df = pd.DataFrame(datos)

print("NORMALIZACIÓN MIN-MAX - INGRESOS ANUALES")
print("="*42)
print("\nDatos originales:")
print(df)

# Normalización
scaler = MinMaxScaler()
df_norm = df.copy()
df_norm[['Edad', 'Ingreso']] = scaler.fit_transform(df[['Edad', 'Ingreso']])

print("\nDatos normalizados [0,1]:")
print(df_norm.round(3))

print("\n✅ Normalización completada!")