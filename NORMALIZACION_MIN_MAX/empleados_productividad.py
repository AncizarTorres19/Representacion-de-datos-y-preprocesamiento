# -*- coding: utf-8 -*-
# Normalización Min-Max - Empleados
# Normalización simple de horas trabajadas y unidades producidas

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Datos de empleados
datos = {
    'Empleado': ['Ana', 'Luis', 'Marta', 'Jorge', 'Sonia', 'Pablo'],
    'Horas_trabajadas': [35, 40, 32, 45, 38, 30],
    'Unidades_producidas': [120, 140, 110, 150, 130, 100]
}

df = pd.DataFrame(datos)

print("NORMALIZACIÓN MIN-MAX - EMPLEADOS")
print("="*40)
print("\nDatos originales:")
print(df)

# Normalización
scaler = MinMaxScaler()
df_norm = df.copy()
df_norm[['Horas_trabajadas', 'Unidades_producidas']] = scaler.fit_transform(df[['Horas_trabajadas', 'Unidades_producidas']])

print("\nDatos normalizados [0,1]:")
print(df_norm.round(3))

print("\n✅ Normalización completada!")