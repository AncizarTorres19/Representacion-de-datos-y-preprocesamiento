# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# ---------------------------
# Utils
# ---------------------------

def imputar_si_bajo_nulos(df, col, estrategia="mean", umbral=0.2):
    """Imputa df[col] si la proporción de NaN es < umbral.
       estrategia: mean | median | mode
    """
    prop_nulos = df[col].isna().mean()
    if prop_nulos < umbral:
        if estrategia == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif estrategia == "median":
            df[col] = df[col].fillna(df[col].median())
        elif estrategia == "mode":
            df[col] = df[col].fillna(df[col].mode()[0])
    # Si >= umbral, puedes decidir otra acción (dejar NaN/eliminar filas/etc.)
    return df

def estado(definitiva):
    if definitiva >= 3:
        return "aprobado"
    if definitiva < 2.5:
        return "reprobado"
    return "habilita"

# ---------------------------
# 1) Ejemplos cortos de imputación con moda y mediana
# ---------------------------

notas_e = {
    "nombres": ["juan", "luis", "farid", "camilo", "esteban"],
    "notas": [3, 2, np.nan, 2, 5]
}
df_notas = pd.DataFrame(notas_e)
# Imputar con moda (tomando el primer valor si hay más de una moda)
df_notas["notas"] = df_notas["notas"].fillna(df_notas["notas"].mode()[0])

edades_data_set = {"edades": [2, 3, 5, 8, 2, 6, np.nan, 6, 9, 5]}
df_edades = pd.DataFrame(edades_data_set)
# Imputar con mediana
df_edades["edades"] = df_edades["edades"].fillna(df_edades["edades"].median())

# ---------------------------
# 2) Notas de clase (bloque principal)
# ---------------------------

notas_clase = {
    "estudiantes": ["Ana", "Luis", "Marta", "Pedro", "Sofia", "Ivan"],
    "notaTaller":  [3.2, 4.8, np.nan, 2.1, 5.0, 4.0],
    "notaQuiz":    [2.9, 4.5, 3.8, np.nan, 4.2, 1.9],
    "Parcial":     [3.5, 4.7, 4.0, 2.4, np.nan, 2.8],
}

notas_df = pd.DataFrame(notas_clase)

# Conteo de nulos
print("NaN por columna en notas_df:")
print(notas_df.isna().sum(), "\n")
# print(notas_df.isna().sum().to_dict())

# 2.1 Imputaciones (usa regla del 20% si quieres; aquí imputamos directo)
notas_df["notaTaller"] = notas_df["notaTaller"].fillna(notas_df["notaTaller"].mean())
notas_df["notaQuiz"]   = notas_df["notaQuiz"].fillna(notas_df["notaQuiz"].mean())

# 2.2 Reglas de negocio ANTES del cálculo de la definitiva
# Piso mínimo para notaQuiz
notas_df.loc[notas_df["notaQuiz"] < 2, "notaQuiz"] = 2

# 2.3 Parcial faltante = promedio fila a fila de Taller y Quiz
notas_df["Parcial"] = notas_df["Parcial"].fillna(
    (notas_df["notaTaller"] + notas_df["notaQuiz"]) / 2
)

# 2.4 Cálculo de definitiva
notas_df["Definitiva"] = (
    notas_df["notaTaller"] * 0.3
    + notas_df["notaQuiz"] * 0.3
    + notas_df["Parcial"] * 0.4
)

# 2.5 Estado
notas_df["Estado"] = notas_df["Definitiva"].apply(estado)

print("Notas con imputación, cap en Quiz, definitiva y estado:")
print(notas_df, "\n")

# ---------------------------
# 3) Imputación por grupo (promedio por sexo)
# ---------------------------

personas = {
    "nombres": ["Ana", "Luis", "Marta", "Pedro", "Sofia"],
    "sexo":    ["f", "m", "f", "m", "f"],
    "edad":    [20, np.nan, 25, 30, np.nan],
}
personas_df = pd.DataFrame(personas)

print("Personas (antes de imputar por grupo):")
print(personas_df, "\n")

personas_df["edad"] = personas_df["edad"].fillna(
    personas_df.groupby("sexo")["edad"].transform("mean")
)

print("Personas (después de imputar por grupo sexo=mean):")
print(personas_df, "\n")

# ---------------------------
# 4) Regla: imputar solo si < 20% de nulos (ejemplo de uso)
# ---------------------------

# Ejemplo: si quisieras aplicar esta regla a 'notaTaller' y 'notaQuiz'
# (Aquí probablemente es < 20%, pero lo dejamos como demostración)
notas_df = imputar_si_bajo_nulos(notas_df, "notaTaller", estrategia="mean", umbral=0.2)
notas_df = imputar_si_bajo_nulos(notas_df, "notaQuiz",   estrategia="mean", umbral=0.2)

# ---------------------------
# 5) Corregido: personas_ingresos (sin claves duplicadas)
# ---------------------------

personas_ingresos = {
    "nombres":  ["Ana", "Luis", "Marta"],
    "edad":     [20, 25, 30],
    "ingresos": [500, 2000, 5000],
}
personas_ingresos_df = pd.DataFrame(personas_ingresos)

print("Personas e ingresos:")
print(personas_ingresos_df)
