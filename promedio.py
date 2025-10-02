import numpy as np
import pandas as pd

# Diccionario con estudiantes y sus edades
datos = {
    "nombres": ["Ana", "Luis", "Maria", "Carlos", "Sofia", "Jorge"],
    "talleres": [3.4, None, 3.8, 4.0, 3.6, None],
    "evaluaciones": [3.4, None, 3.8, 4.0, 3.6, None]
}

print("Datos originales:")
print(datos)

data_frame = pd.DataFrame(datos)
print("\nDataFrame original:")
print(data_frame)

# Listar cuantos valores nulos hay
print("\nConteo de valores nulos por columna:")
print(data_frame.isnull().sum())

# # Eliminar filas con valores nulos
# data_frame_dropna = data_frame.dropna()
# print("\nDataFrame sin valores nulos:")
# print(data_frame_dropna)

# Agregar la moda a los datos None de talleres y media a evaluaciones
moda_talleres = data_frame["talleres"].mode()[0]
media_evaluaciones = data_frame["evaluaciones"].mean()

data_frame["talleres"].fillna(moda_talleres, inplace=True)
data_frame["evaluaciones"].fillna(media_evaluaciones, inplace=True)

# 1. Agregar una nueva columna con el promedio en el data_frame sin valores nulos
data_frame_dropna = data_frame.dropna()
data_frame["promedio"] = (
    data_frame_dropna["talleres"] + data_frame_dropna["evaluaciones"]
) / 2
print("\nDataFrame con columna de promedios:")
print(data_frame)