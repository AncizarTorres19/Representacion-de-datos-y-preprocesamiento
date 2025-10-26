# -*- coding: utf-8 -*-
# Probabilidades con dos dados: Ejercicios 1–4

import numpy as np
import pandas as pd
from fractions import Fraction

# -------------------------------------------------------------
# 
# -------------------------------------------------------------
d1 = np.arange(1, 7)
d2 = np.arange(1, 7)
D1, D2 = np.meshgrid(d1, d2)
D1 = D1.flatten()
D2 = D2.flatten()
df = pd.DataFrame({'dado1': D1, 'dado2': D2})

# Eventos
A = (df['dado1'] + df['dado2']) == 8              # Ej1: suma 8
B = (df['dado1'] == 3) | (df['dado2'] == 3)       # Ej2: al menos un 3
A_y_B = A & B                                      # Ej3: ambos
n_total = len(df)                                  # 36

# -------------------------------------------------------------
# Ejercicio 1: P(suma = 8)
# -------------------------------------------------------------
casos_A = int(A.sum())             # 5 casos: (2,6),(3,5),(4,4),(5,3),(6,2)
P_A = casos_A / n_total
# Forma exacta como fracción
P_A_frac = Fraction(casos_A, n_total)

# -------------------------------------------------------------
# Ejercicio 2: P(al menos un 3)
# -------------------------------------------------------------
casos_B = int(B.sum())             # 11 casos
P_B = casos_B / n_total
P_B_frac = Fraction(casos_B, n_total)

# -------------------------------------------------------------
# Ejercicio 3: P(suma = 8 y al menos un 3) = P(A ∩ B)
# -------------------------------------------------------------
casos_inter = int(A_y_B.sum())     # 2 casos: (3,5),(5,3)
P_inter = casos_inter / n_total
P_inter_frac = Fraction(casos_inter, n_total)

# -------------------------------------------------------------
# Ejercicio 4: P(suma = 8 | al menos un 3) = P(A ∩ B)/P(B)
# -------------------------------------------------------------
P_A_dado_B = P_inter / P_B if P_B > 0 else float('nan')
# también exacto
P_A_dado_B_frac = Fraction(casos_inter, casos_B)

# -------------------------------------------------------------
# Mostrar detalle de casos (útil para capturas/entrega)
# -------------------------------------------------------------
casos_A_list = df.loc[A, ['dado1','dado2']].values.tolist()
casos_B_list = df.loc[B, ['dado1','dado2']].values.tolist()
casos_inter_list = df.loc[A_y_B, ['dado1','dado2']].values.tolist()

print("Total de combinaciones:", n_total)
print("\nEjercicio 1 — P(suma=8)")
print("Casos:", casos_A_list, f" => {casos_A}/{n_total} = {P_A:.6f}  (~{P_A*100:.2f}%)  =", P_A_frac)

print("\nEjercicio 2 — P(al menos un 3)")
print("Casos:", casos_B_list, f" => {casos_B}/{n_total} = {P_B:.6f}  (~{P_B*100:.2f}%)  =", P_B_frac)

print("\nEjercicio 3 — P(suma=8 y ≥ un 3)")
print("Casos:", casos_inter_list, f" => {casos_inter}/{n_total} = {P_inter:.6f}  (~{P_inter*100:.2f}%)  =", P_inter_frac)

print("\nEjercicio 4 — P(suma=8 | ≥ un 3)")
print(f"P(A|B) = P(A∩B)/P(B) = ({casos_inter}/{n_total}) / ({casos_B}/{n_total}) = {P_A_dado_B:.6f}  (~{P_A_dado_B*100:.2f}%)  =", P_A_dado_B_frac)
