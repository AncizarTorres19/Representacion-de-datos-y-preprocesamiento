# -*- coding: utf-8 -*-
# Chatbot - Versión Manual Sin Librerías

# Datos del problema
P_Facil = 0.60                    # 60% fáciles
P_Dificil = 0.40                  # 40% difíciles
P_C_F = 0.70                      # 70% correctas en fáciles
P_C_D = 0.40                      # 40% correctas en difíciles

# Calcular P(Correcta) usando ley de probabilidad total
P_Correcta = (P_C_F * P_Facil) + (P_C_D * P_Dificil)

print("CHATBOT - VERSIÓN MANUAL")
print("="*24)
print("\nDatos:")
print(f"P(Fácil) = {P_Facil} = 3/5")
print(f"P(Difícil) = {P_Dificil} = 2/5")
print(f"P(Correcta|Fácil) = {P_C_F} = 7/10")
print(f"P(Correcta|Difícil) = {P_C_D} = 2/5")

print("\nCálculo (Ley de Probabilidad Total):")
print("P(C) = P(C|F) × P(F) + P(C|D) × P(D)")
print(f"P(C) = {P_C_F} × {P_Facil} + {P_C_D} × {P_Dificil}")
print(f"P(C) = {P_C_F * P_Facil} + {P_C_D * P_Dificil} = {P_Correcta}")

print("\nRESPUESTA:")
print(f"P(Correcta) = {P_Correcta}")
print("Fracción: 29/50")
print(f"Porcentaje: {P_Correcta*100}%")

print(f"\n✅ Precisión global: {P_Correcta*100}%")