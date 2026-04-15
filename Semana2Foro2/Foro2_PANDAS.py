import pandas as pd
ventas = pd.read_csv('ventas.csv')

print(ventas.head())

clientes = pd.read_json('clientes.json')

total_clientes = len(clientes)
print("Total de clientes:", total_clientes)

inventario = pd.read_excel('inventario.xlsx')

promedio_stock = inventario['stock'].mean()
print("Promedio de stock:", promedio_stock)