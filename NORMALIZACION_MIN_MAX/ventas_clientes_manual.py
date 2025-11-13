# -*- coding: utf-8 -*-
# Normalización Min-Max Manual - Ventas y Clientes
# Sin librerías, solo Python puro

# Datos originales
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
clientes = [120, 90, 150, 80, 130]
ventas = [300, 200, 400, 180, 350]

print("NORMALIZACIÓN MIN-MAX MANUAL - VENTAS Y CLIENTES")
print("="*50)
print("\nDatos originales:")
print(f"{'Mes':<10} {'Clientes':<10} {'Ventas':<10}")
print("-" * 35)
for i in range(len(meses)):
    print(f"{meses[i]:<10} {clientes[i]:<10} {ventas[i]:<10}")

# Fórmula: (X - min) / (max - min)
def normalizar(datos):
    min_val = min(datos)
    max_val = max(datos)
    return [(x - min_val) / (max_val - min_val) for x in datos]

# Normalización manual
clientes_norm = normalizar(clientes)
ventas_norm = normalizar(ventas)

print("\nDatos normalizados [0,1]:")
print(f"{'Mes':<10} {'Clientes':<10} {'Ventas':<10}")
print("-" * 35)
for i in range(len(meses)):
    print(f"{meses[i]:<10} {clientes_norm[i]:<10.3f} {ventas_norm[i]:<10.3f}")

print("\n✅ Normalización manual completada!")