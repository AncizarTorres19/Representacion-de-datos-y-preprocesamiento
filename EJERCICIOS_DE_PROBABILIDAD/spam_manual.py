# -*- coding: utf-8 -*-
# Detección de Spam - Versión Manual Sin Librerías

# Datos del problema
P_S = 0.60          # P(Spam) 
P_G = 0.30          # P(contiene "gratis")
P_S_dado_G = 0.80   # P(Spam | "gratis")

print("DETECCIÓN DE SPAM - VERSIÓN MANUAL")
print("="*38)
print("\nDatos del problema:")
print(f"P(Spam) = {P_S} = 60/100")
print(f"P(Gratis) = {P_G} = 30/100") 
print(f"P(Spam|Gratis) = {P_S_dado_G} = 80/100")

print("\nRESPUESTA:")
print(f"P(Spam|Gratis) = {P_S_dado_G}")
print("Fracción: 4/5")
print(f"Porcentaje: {P_S_dado_G*100}%")

print(f"\n✅ De cada 100 correos con 'gratis', {P_S_dado_G*100:.0f} son spam")