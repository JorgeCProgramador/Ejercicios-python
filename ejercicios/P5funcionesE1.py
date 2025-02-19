nombre_producto = input("Introduzca el nombre del producto: ")
precio_producto = float(input("Introduzca el precio del producto: "))
cantidad_producto = int(input("Introduzca la cantidad del producto: "))
descuento_producto = float(input("Introduzca el descuento en porcentaje del producto: "))
iva_producto = float(input("Introduzca el iva en porcentaje del producto: "))

# Aplicar decuento
def descuento(descuento_producto, precio_producto ):
    descuento_final = precio_producto * (descuento_producto/100)
    return descuento_final

#Aplicar el iva
def iva(iva_producto, precio_producto):
    iva_final = precio_producto * (iva_producto/100)
    return iva_final

#Precio final
def precio_final(precio_producto, cantidad_producto):
    descuento_final = precio_producto - descuento(descuento_producto,precio_producto)

    precio = descuento_final * cantidad_producto

    return precio + iva(iva_producto, precio_producto)

precio_total = precio_final(precio_producto, cantidad_producto)
print("El precio final de", nombre_producto, precio_total)