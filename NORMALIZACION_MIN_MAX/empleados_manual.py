# -*- coding: utf-8 -*-
# Normalización Min-Max Manual - Empleados
# Sin librerías, solo Python puro

# Datos de empleados
empleados = ['Ana', 'Luis', 'Marta', 'Jorge', 'Sonia', 'Pablo']
horas = [35, 40, 32, 45, 38, 30]
unidades = [120, 140, 110, 150, 130, 100]

print("NORMALIZACIÓN MIN-MAX MANUAL - EMPLEADOS")
print("="*42)
print("\nDatos originales:")
print(f"{'Empleado':<10} {'Horas':<10} {'Unidades':<10}")
print("-" * 35)
for i in range(len(empleados)):
    print(f"{empleados[i]:<10} {horas[i]:<10} {unidades[i]:<10}")

# Fórmula: (X - min) / (max - min)
def normalizar(datos):
    min_val = min(datos)
    max_val = max(datos)
    return [(x - min_val) / (max_val - min_val) for x in datos]

# Normalización manual
horas_norm = normalizar(horas)
unidades_norm = normalizar(unidades)

print("\nDatos normalizados [0,1]:")
print(f"{'Empleado':<10} {'Horas':<10} {'Unidades':<10}")
print("-" * 35)
for i in range(len(empleados)):
    print(f"{empleados[i]:<10} {horas_norm[i]:<10.3f} {unidades_norm[i]:<10.3f}")

print("\n✅ Normalización manual completada!")