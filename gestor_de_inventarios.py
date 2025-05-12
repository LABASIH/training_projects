# Lista donde se almacenan los productos como diccionarios
inventario = []

# Función para ingresar un nuevo producto al inventario
def ingresar_producto(nombre: str, precio: float, cantidad: int):
    # Bucle que itera sobre la lista verificando que el nombre del producto ingresado no se encuentre en el inventario
    for producto in inventario:
        if producto["nombre"] == nombre.lower(): # El nombre se verificará en minúsculas 
            print("El producto ya existe.")
            return
    try:
        if precio < 0 or cantidad < 0:
            raise ValueError("No se permiten ingresar valores negativos al precio o a la cantidad.") # Imprime el error en caso tal de no cumpli la condición
        # Estructura definida para crear el diccionario dentro de la lista
        nuevo_producto = {
            "nombre": nombre.lower(),
            "precio": precio,
            "cantidad": cantidad
        }
        # Agrega el diccionario dentro de la lista
        inventario.append(nuevo_producto)
        print(f'Producto "{nombre}" agregado correctamente.')
    except ValueError:
        print("Los datos ingresados no corresponden a un precio o cantidad.")

# Función para consultar un producto por su nombre
def consultar_producto(nombre: str):
    """
    Bucle que itera sobre la lista inventario verificando que el nombre del producto ingresado se encuentre allí para luego
    imprimir cada una de las llaves y su valor
    """
    for producto in inventario:
        if producto["nombre"] == nombre.lower():
            print(f'Producto: {producto["nombre"]} | Precio: ${producto["precio"]:.2f} | Cantidad: {producto["cantidad"]}')
            return
    print("Producto no encontrado en el inventario.")

# Función para actualizar el precio de un producto
def actualizar_precio(nombre: str, nuevo_precio: float):
    """
    Bucle que itera sobre la lista inventario verificando que el nombre del producto ingresado exista luego, si el precio es positivo,
    este accederá a la clave 'precio' para modificarla según el argumento ingresado
    """
    for producto in inventario:
        if producto["nombre"] == nombre.lower():
            try:
                if nuevo_precio > 0:
                    producto["precio"] = nuevo_precio
                    print("Precio actualizado correctamente.")
                    return
            except ValueError:
                print("El precio debe ser un número positivo.")
                return

# Función para eliminar un producto del inventario
def eliminar_producto(nombre: str):
    for i, producto in enumerate(inventario): # Se recorre la lista con la ayuda de enumerate, así se consigue obtener el indice actual del producto
        if producto["nombre"] == nombre.lower():
            inventario.pop(i) # Se usa pop(i) para eliminar el producto en la posicición 'i' de la lista
            print("Producto eliminado correctamente.")
            return
    print("Producto no encontrado.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    # Se establece que lambda recibira un parametro que en este caso corresponde tanto al del precio como la cantidad ambos siendo claves en el inventario
    calcular_valor = lambda p: p["precio"] * p["cantidad"]
    total = 0
    # Recorre el inventario y ejecuta a partir de la variable la función lambda para así multiplicar tanto el precio como la cantidad de cada producto iterado
    for producto in inventario:
        valor_producto = calcular_valor(producto)
        total += valor_producto # Se suman y se almacenan en la variable para luego imprimirse
    if total > 0:
        print(f"Valor total del inventario: ${total:.2f}")
    else:
        print("El inventario está vacío.")

# Menú principal de interacción con el usuario
def menu():
    while True:
        print("\n---\ MENÚ DE INVENTARIO /---")
        print("1. Ingresar producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        # Ejecuta la primer función de ingreso de producto por parte del usuario
        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
                ingresar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Debe ingresar valores numéricos válidos para precio y cantidad.")
        # Llama a la función para consultar el producto
        elif opcion == "2":
            nombre = input("Nombre del producto a buscar: ").strip()
            consultar_producto(nombre)
        # Ejecuta la función encargada de actualizar el precio. Pide al usuario que ingrese el nuevo precio del producto
        elif opcion == "3":
            nombre = input("Nombre del producto: ").strip()
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                actualizar_precio(nombre, nuevo_precio)
            except ValueError:
                print("Debe ingresar un número válido para el precio.")
        # Llama a la función que elimina el producto que el usuario haya ingresado
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(nombre)
        # Ejecuta la función que implementa Lambda en orden de calcular el valor total del inventario
        elif opcion == "5":
            calcular_valor_total()
        # Al romper el bucle el programa se cierra
        elif opcion == "6":
            print("Gracias por usar el sistema de inventario.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
