# -*- coding: utf-8 -*-
# Chatbot - Versión Simple con Librerías

import pandas as pd
from fractions import Fraction

# Datos del problema
P_Facil = 0.60                    # 60% fáciles
P_Dificil = 0.40                  # 40% difíciles
P_C_F = 0.70                      # 70% correctas en fáciles
P_C_D = 0.40                      # 40% correctas en difíciles

# Calcular P(Correcta) usando ley de probabilidad total
P_Correcta = (P_C_F * P_Facil) + (P_C_D * P_Dificil)

# Crear DataFrame
datos = {
    'Variable': ['P(Fácil)', 'P(Difícil)', 'P(C|Fácil)', 'P(C|Difícil)', 'P(Correcta)'],
    'Valor': [P_Facil, P_Dificil, P_C_F, P_C_D, P_Correcta],
    'Fracción': ['3/5', '2/5', '7/10', '2/5', '29/50']
}

df = pd.DataFrame(datos)

print("CHATBOT - VERSIÓN SIMPLE")
print("="*26)
print("\nDatos:")
print(df)

print("\nCálculo (Ley de Probabilidad Total):")
print("P(C) = P(C|F) × P(F) + P(C|D) × P(D)")
print(f"P(C) = {P_C_F} × {P_Facil} + {P_C_D} × {P_Dificil}")
print(f"P(C) = {P_C_F * P_Facil} + {P_C_D * P_Dificil} = {P_Correcta}")

print("\nRESPUESTA:")
print(f"P(Correcta) = {P_Correcta}")
print("Fracción: 29/50")
print(f"Porcentaje: {P_Correcta*100}%")

print(f"\n✅ Precisión global: {P_Correcta*100}%")