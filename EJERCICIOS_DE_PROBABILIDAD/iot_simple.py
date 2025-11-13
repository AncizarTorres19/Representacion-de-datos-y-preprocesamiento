# -*- coding: utf-8 -*-
# Sensor IoT - Versión Simple con Librerías

import pandas as pd
from fractions import Fraction

# Datos del problema
P_Lluvia = 0.30                    # P(Llueve)
P_Predice_dado_Lluvia = 0.85       # P(Predice|Llueve)

# Calcular probabilidad conjunta
P_Conjunta = P_Predice_dado_Lluvia * P_Lluvia

# Crear DataFrame
datos = {
    'Evento': ['P(Llueve)', 'P(Predice|Llueve)', 'P(Predice ∩ Llueve)'],
    'Valor': [P_Lluvia, P_Predice_dado_Lluvia, P_Conjunta],
    'Fracción': ['3/10', '17/20', '51/200']
}

df = pd.DataFrame(datos)

print("SENSOR IoT - VERSIÓN SIMPLE")
print("="*30)
print("\nDatos:")
print(df)

print("\nCálculo:")
print("P(Predice ∩ Llueve) = P(Predice|Llueve) × P(Llueve)")
print(f"P(Predice ∩ Llueve) = {P_Predice_dado_Lluvia} × {P_Lluvia} = {P_Conjunta}")

print("\nRESPUESTA:")
print(f"P(Predice ∩ Llueve) = {P_Conjunta}")
print(f"Porcentaje: {P_Conjunta*100}%")

print(f"\n✅ En {P_Conjunta*100}% de los días, predice Y llueve")