# -*- coding: utf-8 -*-
# Normalización Min-Max - Ventas y Clientes
# Normalización simple con sklearn

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Datos originales
datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Clientes': [120, 90, 150, 80, 130],
    'Ventas': [300, 200, 400, 180, 350]
}

df = pd.DataFrame(datos)

print("NORMALIZACIÓN MIN-MAX - VENTAS Y CLIENTES")
print("="*42)
print("\nDatos originales:")
print(df)

# Normalización
scaler = MinMaxScaler()
df_norm = df.copy()
df_norm[['Clientes', 'Ventas']] = scaler.fit_transform(df[['Clientes', 'Ventas']])

print("\nDatos normalizados [0,1]:")
print(df_norm.round(3))

print("\n✅ Normalización completada!")