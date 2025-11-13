# -*- coding: utf-8 -*-
# Ejercicio de Detección de Transacciones Fraudulentas
# Sistema de IA para detectar fraudes en transacciones bancarias

from fractions import Fraction

# -------------------------------------------------------------
# DATOS DEL PROBLEMA
# -------------------------------------------------------------
# Total de transacciones en un día: 50,000
# - 500 son realmente fraudulentas
# - El modelo marca 700 como sospechosas
# - De esas 700 marcadas, 420 resultan ser fraudes reales

total_transacciones = 50000
realmente_fraude = 500          # Transacciones que SÍ son fraude
modelo_marca = 700              # Transacciones que el modelo marca como sospechosas
marcadas_y_fraude = 420         # De las 700 marcadas, cuántas son realmente fraude

# -------------------------------------------------------------
# EVENTOS
# -------------------------------------------------------------
# F = La transacción es realmente fraudulenta
# M = El modelo marca la transacción como sospechosa

# -------------------------------------------------------------
# EJERCICIO 1: P(F) - Probabilidad de fraude real
# -------------------------------------------------------------
P_F = realmente_fraude / total_transacciones
P_F_frac = Fraction(realmente_fraude, total_transacciones)

print("="*70)
print("EJERCICIO: DETECCIÓN DE TRANSACCIONES FRAUDULENTAS")
print("="*70)
print(f"\nTotal de transacciones: {total_transacciones:,}")
print(f"Transacciones realmente fraudulentas: {realmente_fraude}")
print(f"Transacciones marcadas por el modelo: {modelo_marca}")
print(f"De las marcadas, realmente fraudulentas: {marcadas_y_fraude}")
print("\n" + "-"*70)

print("\n1. P(F) - Probabilidad de fraude real:")
print(f"   P(F) = {realmente_fraude}/{total_transacciones} = {P_F:.6f} = {P_F*100:.2f}%")
print(f"   Fracción simplificada: {P_F_frac}")

# -------------------------------------------------------------
# EJERCICIO 2: P(M) - Probabilidad de que el modelo marque
# -------------------------------------------------------------
P_M = modelo_marca / total_transacciones
P_M_frac = Fraction(modelo_marca, total_transacciones)

print("\n2. P(M) - Probabilidad de que el modelo marque una transacción:")
print(f"   P(M) = {modelo_marca}/{total_transacciones} = {P_M:.6f} = {P_M*100:.2f}%")
print(f"   Fracción simplificada: {P_M_frac}")

# -------------------------------------------------------------
# EJERCICIO 3: P(F|M) - Prob. condicional: fraude real SI fue marcada
# -------------------------------------------------------------
# De las 700 transacciones marcadas, 420 son realmente fraude
P_F_dado_M = marcadas_y_fraude / modelo_marca
P_F_dado_M_frac = Fraction(marcadas_y_fraude, modelo_marca)

print("\n3. P(F|M) - Prob. de fraude real SI el modelo marcó:")
print(f"   P(F|M) = {marcadas_y_fraude}/{modelo_marca} = {P_F_dado_M:.6f} = {P_F_dado_M*100:.2f}%")
print(f"   Fracción simplificada: {P_F_dado_M_frac}")
print(f"   Interpretación: De cada 100 transacciones marcadas, ~{P_F_dado_M*100:.1f} son fraudes reales")

# -------------------------------------------------------------
# EJERCICIO 4: P(Error) - Prob. de que el modelo se equivoque
# -------------------------------------------------------------
# El modelo se equivoca cuando:
#   - Marca como fraude algo que NO es fraude (Falso Positivo): M ∩ NoF
#   - NO marca algo que SÍ es fraude (Falso Negativo): NoM ∩ F

# Calculemos todos los escenarios:
# - Marcadas y fraude (F ∩ M): 420
# - Marcadas pero NO fraude (NoF ∩ M): 700 - 420 = 280 [FALSOS POSITIVOS]
# - NO marcadas pero SÍ fraude (F ∩ NoM): 500 - 420 = 80 [FALSOS NEGATIVOS]
# - NO marcadas y NO fraude (NoF ∩ NoM): 50000 - 500 - 280 = 49220

marcadas_no_fraude = modelo_marca - marcadas_y_fraude  # 280 (Falsos Positivos)
no_marcadas_fraude = realmente_fraude - marcadas_y_fraude  # 80 (Falsos Negativos)
no_marcadas_no_fraude = total_transacciones - realmente_fraude - marcadas_no_fraude  # 49220

total_no_marcadas = total_transacciones - modelo_marca  # 49300

# Total de errores = Falsos Positivos + Falsos Negativos
total_errores = marcadas_no_fraude + no_marcadas_fraude
P_Error = total_errores / total_transacciones
P_Error_frac = Fraction(total_errores, total_transacciones)

print("\n4. P(Error) - Probabilidad de que el modelo se equivoque:")
print(f"   Errores totales = Falsos Positivos + Falsos Negativos")
print(f"   Errores = {marcadas_no_fraude} + {no_marcadas_fraude} = {total_errores}")
print(f"   P(Error) = {total_errores}/{total_transacciones} = {P_Error:.6f} = {P_Error*100:.2f}%")
print(f"   Fracción simplificada: {P_Error_frac}")
print(f"   Interpretación: El modelo se equivoca en {P_Error*100:.2f}% de las transacciones")

# -------------------------------------------------------------
# TABLA PARA VISUALIZACIÓN DE RESULTADOS
# -------------------------------------------------------------
print("\n" + "="*70)
print("TABLA PARA VISUALIZACIÓN DE RESULTADOS")
print("="*70)
print(f"{'':25} | {'Marca (M)':>15} | {'NoMarca (NoM)':>15} | {'Total':>15}")
print("-"*70)
print(f"{'Fraude (F)':25} | {marcadas_y_fraude:>15} | {no_marcadas_fraude:>15} | {realmente_fraude:>15}")
print(f"{'No Fraude (NoF)':25} | {marcadas_no_fraude:>15} | {no_marcadas_no_fraude:>15} | {total_transacciones - realmente_fraude:>15}")
print("-"*70)
print(f"{'Total':25} | {modelo_marca:>15} | {total_no_marcadas:>15} | {total_transacciones:>15}")

# -------------------------------------------------------------
# RESUMEN FINAL
# -------------------------------------------------------------
print("\n" + "="*70)
print("RESUMEN DE RESPUESTAS")
print("="*70)
print(f"1. P(F) = {P_F_frac} ≈ {P_F:.6f} ({P_F*100:.2f}%)")
print(f"2. P(M) = {P_M_frac} ≈ {P_M:.6f} ({P_M*100:.2f}%)")
print(f"3. P(F|M) = {P_F_dado_M_frac} ≈ {P_F_dado_M:.6f} ({P_F_dado_M*100:.2f}%)")
print(f"4. P(Error) = {P_Error_frac} ≈ {P_Error:.6f} ({P_Error*100:.2f}%)")
print("="*70)