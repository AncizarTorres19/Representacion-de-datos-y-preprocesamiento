# -*- coding: utf-8 -*-
# Normalización Min-Max - Programas Universitarios
# Normalización simple de tasa de graduación y promedio general

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Datos de programas universitarios
datos = {
    'Programa': ['Ingeniería', 'Medicina', 'Derecho', 'Psicología', 'Economía'],
    'Tasa_graduacion': [78, 85, 72, 80, 88],
    'Promedio_general': [4.2, 4.5, 4.0, 4.3, 4.7]
}

df = pd.DataFrame(datos)

print("NORMALIZACIÓN MIN-MAX - PROGRAMAS UNIVERSITARIOS")
print("="*48)
print("\nDatos originales:")
print(df)

# Normalización
scaler = MinMaxScaler()
df_norm = df.copy()
df_norm[['Tasa_graduacion', 'Promedio_general']] = scaler.fit_transform(df[['Tasa_graduacion', 'Promedio_general']])

print("\nDatos normalizados [0,1]:")
print(df_norm.round(3))

print("\n✅ Normalización completada!")