# 1.​Determinar el estado de aprobación:
# a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100).
# b. Evaluar si está aprobada o reprobada basándose en la calificación ingresada.

while True: # Bucle que se ejecuta hasta que la condición if o elif se cumplan  
    try:
        # Entrada de calificaciones por el usuario
        calificacion = float(input('Ingresar calificación (0 a 100): '))
        if 70 <= calificacion <= 100 : # Condición que valida la calificaión ingresada y que aprueba
            print('Aprobado!')
            break
        elif calificacion < 70: # Condición que valida la calificaión ingresada y que cumple que es reprobada 
            print('Reprobado')
            break
        # Excepciones que impiden ingresar valores que no correspondan a lo solicitado para una calificación
        else:
            print('Ingrese una calificación entre el rango establecido (0 a 100)')
    except ValueError:
            print('El valor ingresado no es valido para una calificación')
            print('Intenta con un número')


# 2.​Calcular el promedio:
# a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas).
# b. Calcular y mostrar el promedio de las calificaciones en la lista.


while True: # Bucle que se ejecuta hasta que el promedio es calculado

    try:
        # Se solicita al usuario ingresar las calificaciones separadas por comas
        in_calificacion = str(input('Ingresa las calificaciones separadas por comas (Ejemplo: 0, 1,2, 3,4): '))
        calificaciones_separadas = in_calificacion.split(",") # Se separan las calificaciones por comas y se almacenan en una nueva variable
        cal_list = []
        
        # Se itera la variable cal por cada una de las calificaciones ya separadas por comas
        for cal in calificaciones_separadas:
            cal_float = float(cal.strip()) # Se convierte a flotante la variable que itera y se eliminan espacios en blanco
            cal_list.append(cal_float) # Se añaden los valores convertidos en flotante a la lista vacia declarada al comienzo

        # Se calcula el promedio sumando directamnete la lista y dividiendola por su cantidad de elementos
        promedio = sum(cal_list) / len(cal_list)
        print('El promedio de tus calificaciones es: ', promedio)
        break
    # Excepciones que impiden ingresar valores que no correspondan a lo solicitado para una calificación
    except ValueError:
        print('Asegúrate de ingresar solo números separados por comas.')


# 3.​Contar calificaciones mayores que un valor específico:
# a. Solicitar al usuario un valor numérico.
# b. Contar y mostrar cuántas calificaciones en la lista son mayores que ese valor.

try: 
    calificacion_mayor = input('ingresar lista de calificaciones separadas por comas (Ejemplo: 0, 1,2, 3,4): ')
    sep_calificaciones = calificacion_mayor.split(',')
    list_cal = []
# 
    for mayor_cal in sep_calificaciones:
        list_cal.append(float(mayor_cal.strip())) # Se convierte a flotante la variable que itera y se eliminan espacios en blanco \
                                                  # Se añaden lo datos de la variable que itera a la lista vacia 


    # Se establece el numero que se va comparar
    mayor = float(input('Ingrese un valor para evaluar cuantas calificaciones son mayores a este: '))
    # Utilización de comprension de listas para establecer el contador que llevara la cuenta de los numeros que cumplen la condición
    contador = sum(1 for mayor_cal in list_cal if mayor_cal > mayor)

    print('Hay',contador,'números mayores que',mayor)

except ValueError:
    print('El valor ingresado no correspondea una calificación')


# 4.​Verificar y contar calificaciones específicas:
# a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas) y una calificación específica.
# b. Contar y mostrar cuántas veces aparece dicha calificación en la lista.

while True:
    try:
        calificaciones_rep = input('Ingresa una lista de calificaciones separadas por comas (Ejemplo: 0, 1, 2, 3, 4): ')
        sep_cal = calificaciones_rep.split(',')

        # Convierte cada dato ingresado a flotante después de quitar espacios, y crea una nueva lista
        lista_calificaciones = [float(cal.strip()) for cal in sep_cal]

        # Se establece el valor a buscar en la lista
        valor_especifico = float(input('Ingresa la calificación que deseas buscar: '))

        # Cuenta en la lista ya con los valores convertidos a flotante el valor especifico establecido anteriormente 
        conteo_cal = lista_calificaciones.count(valor_especifico)

        # Se detiene el bucle y se imprime el valor que se buscaba y la cantidad de veces que se encontró
        print('La calificación',valor_especifico,'aparece',conteo_cal,'veces en la lista.')
        break

    except ValueError:
        print('Asegúrate de ingresar solo números válidos.')
