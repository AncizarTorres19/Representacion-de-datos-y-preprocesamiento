import pandas as pd
import numpy as np

# Primer ejercicio (media):
notas = {"nombres": ["Juan","Luis","Ana"], "nota": [3, np.nan, 4]}
df = pd.DataFrame(notas)

print("-contar nulos", "\n",  df.isna().sum())     # contar nulos
media = df["nota"].mean()  # calcular media
df["nota"] = df["nota"].fillna(media)
print("-df", "\n", df)

# Segundo ejercicio (mediana y dropna):
edades = {"edad": [20, 25, np.nan, 30, 40]}
df2 = pd.DataFrame(edades)

# Imputar con mediana
df2["edad"] = df2["edad"].fillna(df2["edad"].median())
print("-df2", "\n", df2)

# Alternativa: eliminar filas con NaN
df2_drop = df2.dropna()
print("-df2_drop", "\n", df2_drop)

# Tercer ejercicio (varias columnas, promedio):
data = {
    "nombre": ["Ana","Luis","Marta"],
    "nota1": [3, np.nan, 5],
    "nota2": [4, 2, np.nan]
}
df3 = pd.DataFrame(data)

# Imputar diferente en cada columna
df3["nota1"] = df3["nota1"].fillna(df3["nota1"].mean())      # media
df3["nota2"] = df3["nota2"].fillna(df3["nota2"].mode()[0])   # moda

# Crear nueva columna promedio
df3["promedio"] = (df3["nota1"] + df3["nota2"]) / 2
print("-df3", "\n", df3)
