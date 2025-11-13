# -*- coding: utf-8 -*-
# Sensor IoT - Versión Manual Sin Librerías

# Datos del problema
P_Lluvia = 0.30                    # P(Llueve)
P_Predice_dado_Lluvia = 0.85       # P(Predice|Llueve)

# Calcular probabilidad conjunta
P_Conjunta = P_Predice_dado_Lluvia * P_Lluvia

print("SENSOR IoT - VERSIÓN MANUAL")
print("="*28)
print("\nDatos:")
print(f"P(Llueve) = {P_Lluvia} = 3/10")
print(f"P(Predice|Llueve) = {P_Predice_dado_Lluvia} = 17/20")

print("\nCálculo:")
print("P(Predice ∩ Llueve) = P(Predice|Llueve) × P(Llueve)")
print(f"P(Predice ∩ Llueve) = {P_Predice_dado_Lluvia} × {P_Lluvia} = {P_Conjunta}")

print("\nRESPUESTA:")
print(f"P(Predice ∩ Llueve) = {P_Conjunta}")
print("Fracción: 51/200")
print(f"Porcentaje: {P_Conjunta*100}%")

print(f"\n✅ En {P_Conjunta*100}% de los días, predice Y llueve")