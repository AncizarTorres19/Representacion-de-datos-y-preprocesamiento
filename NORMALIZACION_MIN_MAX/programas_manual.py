# -*- coding: utf-8 -*-
# Normalización Min-Max Manual - Programas Universitarios
# Sin librerías, solo Python puro

# Datos de programas universitarios
programas = ['Ingeniería', 'Medicina', 'Derecho', 'Psicología', 'Economía']
graduacion = [78, 85, 72, 80, 88]
promedio = [4.2, 4.5, 4.0, 4.3, 4.7]

print("NORMALIZACIÓN MIN-MAX MANUAL - PROGRAMAS UNIVERSITARIOS")
print("="*56)
print("\nDatos originales:")
print(f"{'Programa':<12} {'Graduación':<12} {'Promedio':<10}")
print("-" * 38)
for i in range(len(programas)):
    print(f"{programas[i]:<12} {graduacion[i]:<12} {promedio[i]:<10}")

# Fórmula: (X - min) / (max - min)
def normalizar(datos):
    min_val = min(datos)
    max_val = max(datos)
    return [(x - min_val) / (max_val - min_val) for x in datos]

# Normalización manual
graduacion_norm = normalizar(graduacion)
promedio_norm = normalizar(promedio)

print("\nDatos normalizados [0,1]:")
print(f"{'Programa':<12} {'Graduación':<12} {'Promedio':<10}")
print("-" * 38)
for i in range(len(programas)):
    print(f"{programas[i]:<12} {graduacion_norm[i]:<12.3f} {promedio_norm[i]:<10.3f}")

print("\n✅ Normalización manual completada!")