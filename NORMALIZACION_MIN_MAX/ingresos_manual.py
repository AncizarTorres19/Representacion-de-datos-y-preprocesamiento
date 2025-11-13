# -*- coding: utf-8 -*-
# Normalización Min-Max Manual - Ingresos Anuales
# Sin librerías, solo Python puro

# Datos de empleados
empleados = ['Andrea', 'Blanca Inés', 'Carla María', 'Viviana Montoya', 'Juan Pérez', 'Iván Cepeda']
edades = [15, 32, 25, 22, 41, 20]
ingresos = [800, 1000, 1200, 5000, 1500, 3500]

print("NORMALIZACIÓN MIN-MAX MANUAL - INGRESOS ANUALES")
print("="*48)
print("\nDatos originales:")
print(f"{'Empleado':<15} {'Edad':<8} {'Ingreso':<10}")
print("-" * 38)
for i in range(len(empleados)):
    print(f"{empleados[i]:<15} {edades[i]:<8} {ingresos[i]:<10}")

# Fórmula: (X - min) / (max - min)
def normalizar(datos):
    min_val = min(datos)
    max_val = max(datos)
    return [(x - min_val) / (max_val - min_val) for x in datos]

# Normalización manual
edades_norm = normalizar(edades)
ingresos_norm = normalizar(ingresos)

print("\nDatos normalizados [0,1]:")
print(f"{'Empleado':<15} {'Edad':<8} {'Ingreso':<10}")
print("-" * 38)
for i in range(len(empleados)):
    print(f"{empleados[i]:<15} {edades_norm[i]:<8.3f} {ingresos_norm[i]:<10.3f}")

print("\n✅ Normalización manual completada!")