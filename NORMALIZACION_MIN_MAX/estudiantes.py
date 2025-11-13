# -*- coding: utf-8 -*-
# Normalización Min-Max - Estudiantes
# Normalización simple de asistencia y nota final

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Datos de estudiantes
datos = {
    'Estudiante': ['Laura', 'Andrés', 'Diana', 'Felipe', 'Natalia'],
    'Porcentaje_Asistencia': [90, 75, 60, 95, 85],
    'Nota_final': [4.8, 4.0, 3.2, 5.0, 4.5]
}

df = pd.DataFrame(datos)

print("NORMALIZACIÓN MIN-MAX - ESTUDIANTES")
print("="*38)
print("\nDatos originales:")
print(df)

# Normalización
scaler = MinMaxScaler()
df_norm = df.copy()
df_norm[['Porcentaje_Asistencia', 'Nota_final']] = scaler.fit_transform(df[['Porcentaje_Asistencia', 'Nota_final']])

print("\nDatos normalizados [0,1]:")
print(df_norm.round(3))

print("\n✅ Normalización completada!")