# -*- coding: utf-8 -*-
# Visión por Computador - Versión Simple con Librerías

import pandas as pd
from fractions import Fraction

# Datos del problema  
precision = 0.92                   # Precisión del 92%
P_F = 0.40                        # 40% femeninas
P_M = 0.60                        # 60% masculinas

# Calcular P(error|F)
P_error_F = 1 - precision

# Crear DataFrame
datos = {
    'Métrica': ['Precisión', 'P(Femenina)', 'P(Error|Femenina)'],
    'Valor': [precision, P_F, P_error_F],
    'Fracción': ['23/25', '2/5', '2/25']
}

df = pd.DataFrame(datos)

print("VISIÓN POR COMPUTADOR - VERSIÓN SIMPLE")
print("="*40)
print("\nDatos:")
print(df)

print("\nCálculo:")
print("P(Error|F) = 1 - Precisión")
print(f"P(Error|F) = 1 - {precision} = {P_error_F}")

print("\nRESPUESTA:")
print(f"P(Error|F) = {P_error_F}")
print("Fracción: 2/25")
print(f"Porcentaje: {P_error_F*100}%")

print(f"\n✅ El modelo se equivoca en {P_error_F*100}% de imágenes femeninas")