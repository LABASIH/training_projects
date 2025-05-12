# -*- coding: utf-8 -*-
# Inicializamos la biblioteca como una lista vacía.
# Cada libro será un diccionario dentro de esta lista.
biblioteca = []

# Definimos los géneros permitidos para validar las entradas.
# Se almacenan con la primera letra en mayúscula, pero la comparación será insensible al caso.
GENEROS_PERMITIDOS = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

def anadir_libro():
    """
    Permite al usuario agregar un nuevo libro a la biblioteca.
    Solicita título, autor, cantidad de copias y género.
    Valida que el género esté en la lista de géneros permitidos (de forma insensible a mayúsculas/minúsculas).
    Verifica si el libro (por título) ya existe para evitar duplicados.
    """
    print("\n--- Añadir nuevo libro ---")
    # Solicitamos el título y lo convertimos a minúsculas para una comparación y almacenamiento consistentes.
    titulo = input("Ingrese el título del libro: ").strip().lower()

    # Verificamos si un libro con el mismo título ya existe.
    for libro_existente in biblioteca: # Renombrada la variable para evitar confusión con 'libro' más adelante
        if libro_existente['titulo'] == titulo:
            print(f"Error: El libro con el título '{titulo}' ya existe en la biblioteca.")
            return # Salimos de la función si el libro ya existe.

    # Si el libro no existe, solicitamos el resto de los detalles.
    autor = input("Ingrese el autor del libro: ").strip()

    # Solicitamos la cantidad de copias, asegurándonos de que sea un número entero positivo.
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de copias disponibles: "))
            if cantidad > 0:
                break
            else:
                print("Error: La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad.")

    # Solicitamos el género y validamos que esté en la lista de géneros permitidos.
    genero_valido = None
    while True:
        print(f"Géneros disponibles: {', '.join(GENEROS_PERMITIDOS)}")
        genero_input = input("Ingrese el género del libro: ").strip()
        # Comparamos de forma insensible a mayúsculas/minúsculas
        for genero_permitido in GENEROS_PERMITIDOS:
            if genero_input.lower() == genero_permitido.lower():
                genero_valido = genero_permitido # Usamos el formato de la lista para almacenar
                break
        if genero_valido:
            break
        else:
            print(f"Error: Género '{genero_input}' no válido. Por favor, elija uno de la lista.")

    # Creamos un diccionario para el nuevo libro.
    nuevo_libro = {
        'titulo': titulo, # Se almacena en minúsculas
        'autor': autor,
        'cantidad_total': cantidad,
        'cantidad_disponible': cantidad,
        'genero': genero_valido # Se almacena el género con el formato de la lista
    }

    # Añadimos el nuevo libro a la lista de la biblioteca.
    biblioteca.append(nuevo_libro)
    print(f"¡Libro '{titulo}' añadido exitosamente a la biblioteca!") # Se muestra en minúsculas

def buscar_libro():
    """
    Permite al usuario buscar un libro por su título.
    Muestra los detalles del libro si se encuentra (autor, copias disponibles, género).
    Si el libro no se encuentra, muestra un mensaje de error en inglés.
    """
    print("\n--- Buscar libro por título ---")
    titulo_buscar = input("Ingrese el título del libro que desea buscar: ").strip().lower()

    # Recorremos la biblioteca buscando el libro por título.
    for libro in biblioteca:
        if libro['titulo'] == titulo_buscar:
            print("\n--- Detalles del Libro ---")
            print(f"Título: {libro['titulo']}") # Se muestra en minúsculas
            print(f"Autor: {libro['autor']}")
            print(f"Cantidad Disponible: {libro['cantidad_disponible']}")
            print(f"Género: {libro['genero']}")
            return # Salimos de la función una vez encontrado el libro.

    # Si el bucle termina sin encontrar el libro, mostramos un mensaje.
    print(f"Book with title '{titulo_buscar}' not found.") # Mensaje en inglés.

def prestar_libro():
    """
    Registra el préstamo de un libro.
    Disminuye en 1 la cantidad de copias disponibles.
    Valida que haya copias disponibles antes de prestar.
    """
    print("\n--- Prestar libro ---")
    titulo_prestar = input("Ingrese el título del libro que desea prestar: ").strip().lower()

    # Buscamos el libro en la biblioteca.
    for libro in biblioteca:
        if libro['titulo'] == titulo_prestar:
            # Verificamos si hay copias disponibles.
            if libro['cantidad_disponible'] > 0:
                libro['cantidad_disponible'] -= 1 # Disminuimos la cantidad disponible.
                print(f"Préstamo registrado. Una copia de '{libro['titulo']}' ha sido prestada.") # Se muestra en minúsculas
                print(f"Copias restantes de '{libro['titulo']}': {libro['cantidad_disponible']}")
            else:
                print(f"Error: No hay copias disponibles de '{libro['titulo']}' para prestar.")
            return

    # Si no se encuentra el libro.
    print(f"Book with title '{titulo_prestar}' not found.") # Mensaje en inglés.

def devolver_libro():
    """
    Registra la devolución de un libro.
    Aumenta en 1 la cantidad de copias disponibles.
    Valida que la cantidad disponible no exceda la cantidad total de copias que originalmente tenía el libro.
    """
    print("\n--- Devolver libro ---")
    titulo_devolver = input("Ingrese el título del libro que desea devolver: ").strip().lower()

    # Buscamos el libro en la biblioteca.
    for libro in biblioteca:
        if libro['titulo'] == titulo_devolver:
            # Verificamos si se pueden devolver más copias (no exceder el total original).
            if libro['cantidad_disponible'] < libro['cantidad_total']:
                libro['cantidad_disponible'] += 1 # Aumentamos la cantidad disponible.
                print(f"Devolución registrada. Una copia de '{libro['titulo']}' ha sido devuelta.") # Se muestra en minúsculas
                print(f"Copias disponibles de '{libro['titulo']}': {libro['cantidad_disponible']}")
            else:
                print(f"Error: No se pueden devolver más copias de '{libro['titulo']}'. Ya están todas las copias originales en la biblioteca.")
            return

    # Si no se encuentra el libro.
    print(f"Book with title '{titulo_devolver}' not found.") # Mensaje en inglés.

def eliminar_libro():
    """
    Permite eliminar un libro del catálogo.
    Solo se puede eliminar si todas las copias originales están disponibles (es decir, cantidad disponible == cantidad total).
    """
    print("\n--- Eliminar libro del catálogo ---")
    titulo_eliminar = input("Ingrese el título del libro que desea eliminar: ").strip().lower()

    libro_encontrado = None
    indice_libro = -1

    # Buscamos el libro y su índice.
    for i, libro in enumerate(biblioteca):
        if libro['titulo'] == titulo_eliminar:
            libro_encontrado = libro
            indice_libro = i
            break

    if libro_encontrado:
        # Verificamos si el libro tiene copias prestadas.
        if libro_encontrado['cantidad_disponible'] == libro_encontrado['cantidad_total']:
            # Si no hay copias prestadas, eliminamos el libro.
            confirmacion = input(f"¿Está seguro de que desea eliminar '{libro_encontrado['titulo']}'? (s/n): ").strip().lower() # Se muestra en minúsculas
            if confirmacion == 's':
                biblioteca.pop(indice_libro)
                print(f"Libro '{libro_encontrado['titulo']}' eliminado del catálogo.") # Se muestra en minúsculas
            else:
                print("Eliminación cancelada.")
        else:
            print(f"Error: No se puede eliminar '{libro_encontrado['titulo']}' porque tiene copias prestadas.") # Se muestra en minúsculas
            print(f"Copias disponibles: {libro_encontrado['cantidad_disponible']}, Copias totales originales: {libro_encontrado['cantidad_total']}")
    else:
        print(f"Book with title '{titulo_eliminar}' not found.") # Mensaje en inglés.

def listar_libros_por_genero():
    """
    Muestra todos los libros disponibles de un género específico.
    La búsqueda de género es insensible a mayúsculas/minúsculas.
    """
    print("\n--- Listar libros por género ---")
    # Mostramos los géneros disponibles para que el usuario elija.
    print(f"Géneros disponibles: {', '.join(GENEROS_PERMITIDOS)}")
    genero_buscar_input = input("Ingrese el género que desea listar: ").strip()

    genero_encontrado_en_lista = None
    # Comparamos de forma insensible a mayúsculas/minúsculas con la lista de géneros permitidos
    for gen_permitido in GENEROS_PERMITIDOS:
        if genero_buscar_input.lower() == gen_permitido.lower():
            genero_encontrado_en_lista = gen_permitido # Usamos la forma de la lista para filtrar
            break

    if not genero_encontrado_en_lista:
        print(f"Error: Género '{genero_buscar_input}' no válido.")
        return

    # Filtramos los libros por el género especificado (usando el género con la capitalización de la lista).
    libros_del_genero = [libro for libro in biblioteca if libro['genero'] == genero_encontrado_en_lista and libro['cantidad_disponible'] > 0]

    if libros_del_genero:
        print(f"\n--- Libros disponibles del género: {genero_encontrado_en_lista} ---")
        for libro in libros_del_genero:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Copias Disponibles: {libro['cantidad_disponible']}") # Título se muestra en minúsculas
    else:
        print(f"No hay libros disponibles del género '{genero_encontrado_en_lista}' en este momento.")

def mostrar_resumen_inventario():
    """
    Muestra un resumen del inventario:
    - Cuántos títulos de libros diferentes hay en total.
    - Cuántas copias de libros en total están disponibles en la biblioteca.
    """
    print("\n--- Resumen del Inventario ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return

    total_titulos_diferentes = len(biblioteca) # Cada entrada en la lista 'biblioteca' es un título único.
    total_copias_disponibles = 0
    for libro in biblioteca:
        total_copias_disponibles += libro['cantidad_disponible']

    print(f"Total de títulos de libros diferentes en la biblioteca: {total_titulos_diferentes}")
    print(f"Total de copias de libros disponibles en la biblioteca: {total_copias_disponibles}")


def menu():
    """
    Muestra el menú principal y gestiona las opciones del usuario.
    Permite agregar al menos 10 libros (esto se cumple si el usuario usa la opción 1 repetidamente).
    """
    while True:
        print("\n------ MENÚ DE LA BIBLIOTECA COMUNITARIA ------")
        print("1. Añadir libro a la biblioteca")
        print("2. Buscar libro por título")
        print("3. Registrar préstamo de libro")
        print("4. Registrar devolución de libro")
        print("5. Eliminar libro del catálogo")
        print("6. Listar libros por género")
        print("7. Mostrar resumen del inventario")
        print("8. Salir del sistema")
        print("---------------------------------------------")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ").strip()

        if opcion == '1':
            anadir_libro()
        elif opcion == '2':
            buscar_libro()
        elif opcion == '3':
            prestar_libro()
        elif opcion == '4':
            devolver_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            listar_libros_por_genero()
        elif opcion == '7':
            mostrar_resumen_inventario()
        elif opcion == '8':
            print("Saliendo del sistema de biblioteca. ¡Hasta pronto!")
            break # Termina el bucle y el programa.
        else:
            print("Opción no válida. Por favor, intente de nuevo ingresando un número del 1 al 8.")

# --- Ejecución Principal ---
# Esta es la parte del código que se ejecuta cuando corres el script.
if __name__ == "__main__":
    # Puedes añadir algunos libros de ejemplo aquí para probar rápidamente si lo deseas:
    # biblioteca.append({'titulo': 'cien años de soledad', 'autor': 'Gabriel García Márquez', 'cantidad_total': 5, 'cantidad_disponible': 3, 'genero': 'Fiction'})
    # biblioteca.append({'titulo': 'sapiens', 'autor': 'Yuval Noah Harari', 'cantidad_total': 3, 'cantidad_disponible': 3, 'genero': 'Non-Fiction'})

    menu() # Llamamos a la función menu para iniciar el programa.