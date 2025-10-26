# -*- coding: utf-8 -*-
# Ejercicio de Reconocimiento Facial en Aeropuerto
# Sistema de identificación de pasajeros con alertas de seguridad

from fractions import Fraction

# -------------------------------------------------------------
# DATOS DEL PROBLEMA
# -------------------------------------------------------------
# Total de personas: 10,000
# - 100 están realmente en la lista de alerta
# - El sistema marca a 150 personas como alerta
# - De esas 150 marcadas, 80 son realmente sospechosas

total_personas = 10000
realmente_alerta = 100          # Personas que SÍ están en lista de alerta
sistema_marca = 150             # Personas que el sistema marca como alerta
marcados_y_sospechosos = 80     # De los 150 marcados, cuántos son realmente sospechosos

# -------------------------------------------------------------
# EVENTOS
# -------------------------------------------------------------
# A = La persona está realmente en la lista de alerta
# Marca = El sistema marca a la persona como alerta

# -------------------------------------------------------------
# EJERCICIO 1: P(A) - Probabilidad de estar en lista de alerta
# -------------------------------------------------------------
P_A = realmente_alerta / total_personas
P_A_frac = Fraction(realmente_alerta, total_personas)

print("="*70)
print("EJERCICIO: RECONOCIMIENTO FACIAL EN AEROPUERTO")
print("="*70)
print(f"\nTotal de personas: {total_personas}")
print(f"Personas realmente en lista de alerta: {realmente_alerta}")
print(f"Personas marcadas por el sistema: {sistema_marca}")
print(f"De las marcadas, realmente sospechosas: {marcados_y_sospechosos}")
print("\n" + "-"*70)

print("\n1. P(A) - Probabilidad de que una persona esté en la lista de alerta:")
print(f"   P(A) = {realmente_alerta}/{total_personas} = {P_A:.6f} = {P_A*100:.2f}%")
print(f"   Fracción simplificada: {P_A_frac}")

# -------------------------------------------------------------
# EJERCICIO 2: P(Marca) - Probabilidad de que el sistema marque
# -------------------------------------------------------------
P_Marca = sistema_marca / total_personas
P_Marca_frac = Fraction(sistema_marca, total_personas)

print("\n2. P(Marca) - Probabilidad de que el sistema marque a alguien:")
print(f"   P(Marca) = {sistema_marca}/{total_personas} = {P_Marca:.6f} = {P_Marca*100:.2f}%")
print(f"   Fracción simplificada: {P_Marca_frac}")

# -------------------------------------------------------------
# EJERCICIO 3: P(A|Marca) - Prob. condicional: estar en lista SI fue marcado
# -------------------------------------------------------------
# De las 150 personas marcadas, 80 son realmente sospechosas
P_A_dado_Marca = marcados_y_sospechosos / sistema_marca
P_A_dado_Marca_frac = Fraction(marcados_y_sospechosos, sistema_marca)

print("\n3. P(A|Marca) - Prob. de estar en lista SI el sistema marcó:")
print(f"   P(A|Marca) = {marcados_y_sospechosos}/{sistema_marca} = {P_A_dado_Marca:.6f} = {P_A_dado_Marca*100:.2f}%")
print(f"   Fracción simplificada: {P_A_dado_Marca_frac}")
print(f"   Interpretación: De cada 100 personas marcadas, ~{P_A_dado_Marca*100:.1f} están realmente en la lista")

# -------------------------------------------------------------
# EJERCICIO 4: P(NoA|NoMarca) - Valor Predictivo Negativo
# -------------------------------------------------------------
# NoA = No está en la lista de alerta
# NoMarca = El sistema NO marca a la persona

# Calculemos todos los escenarios:
# - Marcados y sospechosos (A ∩ Marca): 80
# - Marcados pero NO sospechosos (NoA ∩ Marca): 150 - 80 = 70
# - NO marcados pero SÍ sospechosos (A ∩ NoMarca): 100 - 80 = 20
# - NO marcados y NO sospechosos (NoA ∩ NoMarca): 10000 - 100 - 70 = 9830

marcados_no_sospechosos = sistema_marca - marcados_y_sospechosos  # 70
no_marcados_sospechosos = realmente_alerta - marcados_y_sospechosos  # 20
no_marcados_no_sospechosos = total_personas - realmente_alerta - marcados_no_sospechosos  # 9830

total_no_marcados = total_personas - sistema_marca  # 9850

P_NoA_dado_NoMarca = no_marcados_no_sospechosos / total_no_marcados
P_NoA_dado_NoMarca_frac = Fraction(no_marcados_no_sospechosos, total_no_marcados)

print("\n4. P(NoA|NoMarca) - Valor Predictivo Negativo:")
print(f"   (Probabilidad de NO estar en lista SI el sistema NO marcó)")
print(f"   P(NoA|NoMarca) = {no_marcados_no_sospechosos}/{total_no_marcados} = {P_NoA_dado_NoMarca:.6f} = {P_NoA_dado_NoMarca*100:.4f}%")
print(f"   Fracción simplificada: {P_NoA_dado_NoMarca_frac}")
print(f"   Interpretación: Si el sistema NO marca, hay {P_NoA_dado_NoMarca*100:.4f}% de probabilidad de estar limpio")

# -------------------------------------------------------------
# TABLA DE CONTINGENCIA (para visualización)
# -------------------------------------------------------------
print("\n" + "="*70)
print("TABLA DE CONTINGENCIA")
print("="*70)
print(f"{'':20} | {'Marca':>15} | {'NoMarca':>15} | {'Total':>15}")
print("-"*70)
print(f"{'Alerta (A)':20} | {marcados_y_sospechosos:>15} | {no_marcados_sospechosos:>15} | {realmente_alerta:>15}")
print(f"{'No Alerta (NoA)':20} | {marcados_no_sospechosos:>15} | {no_marcados_no_sospechosos:>15} | {total_personas - realmente_alerta:>15}")
print("-"*70)
print(f"{'Total':20} | {sistema_marca:>15} | {total_no_marcados:>15} | {total_personas:>15}")

# -------------------------------------------------------------
# MÉTRICAS ADICIONALES DEL SISTEMA (bonus)
# -------------------------------------------------------------
print("\n" + "="*70)
print("MÉTRICAS DEL SISTEMA (bonus)")
print("="*70)

# Sensibilidad (Recall): De los que están en lista, ¿cuántos detecta?
sensibilidad = marcados_y_sospechosos / realmente_alerta
print(f"Sensibilidad (Recall): {sensibilidad:.4f} = {sensibilidad*100:.2f}%")
print(f"  → De cada 100 personas en lista, el sistema detecta {sensibilidad*100:.1f}")

# Especificidad: De los que NO están en lista, ¿cuántos NO marca?
especificidad = no_marcados_no_sospechosos / (total_personas - realmente_alerta)
print(f"Especificidad: {especificidad:.4f} = {especificidad*100:.4f}%")
print(f"  → De cada 100 personas limpias, el sistema deja pasar {especificidad*100:.2f}")

# Precisión (Precision): De los marcados, ¿cuántos son realmente sospechosos?
precision = marcados_y_sospechosos / sistema_marca
print(f"Precisión (Precision): {precision:.4f} = {precision*100:.2f}%")
print(f"  → De cada 100 marcados, {precision*100:.1f} son realmente sospechosos")

# Tasa de Falsos Positivos
falsos_positivos = marcados_no_sospechosos / (total_personas - realmente_alerta)
print(f"Tasa de Falsos Positivos: {falsos_positivos:.6f} = {falsos_positivos*100:.4f}%")
print(f"  → {marcados_no_sospechosos} personas inocentes fueron marcadas incorrectamente")

# Tasa de Falsos Negativos
falsos_negativos = no_marcados_sospechosos / realmente_alerta
print(f"Tasa de Falsos Negativos: {falsos_negativos:.4f} = {falsos_negativos*100:.2f}%")
print(f"  → {no_marcados_sospechosos} personas sospechosas pasaron sin ser detectadas")

print("\n" + "="*70)
print("RESUMEN DE RESPUESTAS")
print("="*70)
print(f"1. P(A) = {P_A_frac} ≈ {P_A:.6f}")
print(f"2. P(Marca) = {P_Marca_frac} ≈ {P_Marca:.6f}")
print(f"3. P(A|Marca) = {P_A_dado_Marca_frac} ≈ {P_A_dado_Marca:.6f}")
print(f"4. P(NoA|NoMarca) = {P_NoA_dado_NoMarca_frac} ≈ {P_NoA_dado_NoMarca:.6f}")
print("="*70)
