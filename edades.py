import numpy as np
import pandas as pd

# Diccionario con estudiantes y sus edades
estudiantes = {
    "edades": [23, 25, None, 22],
}

print("Datos originales:")
print(estudiantes)

data_frame = pd.DataFrame(estudiantes)
print("\nDataFrame original:")
print(data_frame)

# Eliminar filas con valores nulos
data_frame_dropna = data_frame.dropna()
print("\nDataFrame sin valores nulos:")
print(data_frame_dropna)

# 1. Calcular la mediana de las edades válidas
mediana = data_frame["edades"].median()
print(f"\nMediana de las edades validas: {mediana}")

# 2. Reemplazar los valores faltantes por la mediana
data_frame["edades"] = data_frame["edades"].fillna(mediana)
print("\nDataFrame con edades corregidas:")
print(data_frame)