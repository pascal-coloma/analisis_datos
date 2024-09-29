import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


ventas = pd.read_csv('C:\\Users\\colom\\Desktop\\Programming\\Data Analysis\\venta_productos\\supermarket_sales.csv')

prod_mas_vendido = ventas['Product line'].value_counts()
cantidad = ventas['Quantity'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=prod_mas_vendido.index, y=prod_mas_vendido.values, palette='viridis')

plt.title('Linea de productos mas vendida')
plt.xlabel('Producto')
plt.ylabel('Cantidad vendida')
plt.xticks(rotation=15)
plt.show()

inc_by_prod = ventas.groupby('Product line')['gross income'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=inc_by_prod.index, y=inc_by_prod.values, palette='coolwarm')

plt.title('Ingresos totales por producto')
plt.xlabel('Producto')
plt.ylabel('Ingreso total')
plt.xticks(rotation=15)
plt.show()

ventas_fecha = ventas.groupby('Date')['Quantity'].sum()

plt.figure(figsize=(12,6))
ventas_fecha.plot(kind='line', color='blue', marker='o')
plt.title('Tendencia de ventas en el tiempo')
plt.xlabel('Fecha')
plt.ylabel('Cantidad')
plt.grid(True)
plt.show()
