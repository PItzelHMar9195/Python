"""
* Haz un programa que pida el precio de un producto
* y el porcentaje de descuento, y calcule el precio 
* final.
"""

#Mensaje
print("\n\n\t\t**** CALCULANDO EL PRECIO FINAL ****\n")

#Lectura de datos
precio = float(input("\t\tINGRESA EL PRECIO DEL PRODUCTO: "))
descuento = float(input("\t\tINGRESA EL PORCENTAJE DE DESCUENTO: "))

#Se calcula el precio final
print(f"\n\t\tEL PRECIO FINAL ES: {precio - (precio * (descuento/100))}\n")