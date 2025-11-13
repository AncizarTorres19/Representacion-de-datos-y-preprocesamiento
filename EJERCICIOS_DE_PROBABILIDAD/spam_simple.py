# -*- coding: utf-8 -*-
# Detección de Spam - Versión Simple con Librerías

import pandas as pd
from fractions import Fraction

# Datos del problema
P_S = 0.60          # P(Spam)
P_G = 0.30          # P(contiene "gratis")
P_S_dado_G = 0.80   # P(Spam | "gratis")

# Crear DataFrame para mostrar datos
datos = {
    'Probabilidad': ['P(Spam)', 'P(Gratis)', 'P(Spam|Gratis)'],
    'Valor': [P_S, P_G, P_S_dado_G],
    'Fracción': [Fraction(60,100), Fraction(30,100), Fraction(80,100)]
}

df = pd.DataFrame(datos)

print("DETECCIÓN DE SPAM - VERSIÓN SIMPLE")
print("="*40)
print("\nDatos del problema:")
print(df)

print("\nRESPUESTA:")
print(f"P(Spam|Gratis) = {P_S_dado_G}")
print(f"Fracción: {Fraction(80,100)}")
print(f"Porcentaje: {P_S_dado_G*100}%")

print(f"\n✅ De cada 100 correos con 'gratis', {P_S_dado_G*100:.0f} son spam")