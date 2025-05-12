# // Se solicita al usuario ingresar un producto
try:
    producto = str(input("Ingresa el nombre del producto: "))
except:
    print('Debes ingresar un nombre en texto')
    exit()


# // Se valida el precio ingresado
try:
    precio = float(input("Ingresa el valor del producto: $"))
    # Aviso en caso de que el usuario ingrese un número negativo
    if precio <= 0:
        print('El precio debe ser un número positivo')
        precio=None
# En caso de que el usuario no ingrese un valor numérico cierra el programa
except ValueError:
    print('Debes ingresar números para el precio')
    exit()
    
    
# // Se valida la cantidad ingresada
try:    
    cantidad = (int(input("Ingrese la cantidad del producto: ")))
    # Aviso en caso de que la cantidad no sea un entero positivo
    if cantidad <= 0:
        print('La cantidad debe ser un entero positivo')
        cantidad=None
# En caso de que el usuario no ingrese un entero positivo cierra el programa
except:
    print('Debes ingresar una cantidad valida')
    exit()

# Validación de datos para aplicar el descuento
try:
    descuento = float(input("Ingresa el descuento del producto: "))
    # En caso de que el descuento ingresado sea menor que 0 y mayor que 100
    if  not(0 <= descuento <= 100):
            print('El valor del descuento debe estar en el rango de 0 a 100 %')
            print('No se aplicará ningún descuento')
# En caso de que el valor ingresado no corresponda a un número
except ValueError:
    print('El valor ingresado no es valido para descuento')
    print('No se aplicará ningún descuento')
    descuento = 0


# // Calculo de precios
precio_sin_descuento = precio * cantidad
descuento_aplicado = precio_sin_descuento * (descuento/100)
precio_con_descuento = precio_sin_descuento - descuento_aplicado


# // Resumen de la compra 
print("\n------ Resumen de compra ------")
print("Producto registrado:", producto)
print("Cantidad del producto registrado und.", cantidad)
print("Volor sin descuento", "$", precio_sin_descuento )
print('El descuento es de $',descuento_aplicado)
print("Valor con descuento del", descuento,"%",':',"$",precio_con_descuento)            