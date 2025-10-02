import numpy as np
import pandas as pd

# Diccionario con estudiantes y sus notas
estudiantes = {
    "nombres": ["Ana", "Luis", "Maria"],
    "notas": [3.4, None, 3.8]
}

print("Datos originales:")
print(estudiantes)

data_frame = pd.DataFrame(estudiantes)
print("\nDataFrame original:")
print(data_frame)

# 1. Calcular la media de las notas válidas
media = data_frame["notas"].mean()
moda = data_frame["notas"].mode()[0]

print(f"\nMedia de las notas validas: {media}")
print(f"Moda de las notas validas: {moda}")

# 2. Reemplazar los valores faltantes por la media
data_frame["notas"] = data_frame["notas"].fillna(media)

print("\nDataFrame con notas corregidas:")
print(data_frame)