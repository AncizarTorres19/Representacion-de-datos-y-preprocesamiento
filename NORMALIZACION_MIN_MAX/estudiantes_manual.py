# -*- coding: utf-8 -*-
# Normalización Min-Max Manual - Estudiantes
# Sin librerías, solo Python puro

# Datos de estudiantes
estudiantes = ['Laura', 'Andrés', 'Diana', 'Felipe', 'Natalia']
asistencia = [90, 75, 60, 95, 85]
notas = [4.8, 4.0, 3.2, 5.0, 4.5]

print("NORMALIZACIÓN MIN-MAX MANUAL - ESTUDIANTES")
print("="*44)
print("\nDatos originales:")
print(f"{'Estudiante':<12} {'Asistencia':<12} {'Nota':<8}")
print("-" * 35)
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]:<12} {asistencia[i]:<12} {notas[i]:<8}")

# Fórmula: (X - min) / (max - min)
def normalizar(datos):
    min_val = min(datos)
    max_val = max(datos)
    return [(x - min_val) / (max_val - min_val) for x in datos]

# Normalización manual
asistencia_norm = normalizar(asistencia)
notas_norm = normalizar(notas)

print("\nDatos normalizados [0,1]:")
print(f"{'Estudiante':<12} {'Asistencia':<12} {'Nota':<8}")
print("-" * 35)
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]:<12} {asistencia_norm[i]:<12.3f} {notas_norm[i]:<8.3f}")

print("\n✅ Normalización manual completada!")