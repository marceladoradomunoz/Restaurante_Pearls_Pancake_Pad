# -*- coding: utf-8 -*-
"""PROGRAMA_RESTAURANTE_M.M.D.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12QoQlRf6RFjb_1eCxctbhBqPChu-8B9a
"""

########CÓDIGO PROGRAMA GESTIÓN RESTAURANTE PEARL´S PANCAKE PAD########

#Cartas de productos creadas en lista de diccionarios donde cada uno tiene 2 claves.
#Clave nombre que identifica la categoría (desayunos, alimentos, bebestibles, postres)
#y el otro la clave productos. Productos, al ser otro diccionario, tiene como clave
#un nº y como valor una tupla que anida el nombre y precio del producto.-
cartas = [
    {
        'name': 'Bfast',
        'products': {
            '1': ('Desayuno continental', 6990),
            '2': ('Desayuno americano', 7990),
            '3': ('Desayuno francés', 8990),
            '4': ('Expresso/Huevos benedictinos', 9990)
        }
    },
    {
        'name': 'Lunches',
        'products': {
            '5': ('Lasagna', 12990),
            '6': ('Pavo asado/Guarniciones', 11990),
            '7': ('Ceviche', 7990),
            '8': ('Risotto de calabaza', 5990),
            '9': ('Filete de vacuno/papas rústicas', 9990),
            '10': ('Salmón/ensaladas de estación', 11990)
        }
    },
    {
        'name': 'Drinks',
        'products': {
            '11': ('Coca-Cola', 1990),
            '12': ('Fanta', 1990),
            '13': ('Sprite', 1990),
            '14': ('Soda mineral/con y sin gas', 1990),
            '15': ('Vino/tinto o blanco', 8990),
            '16': ('Espumante', 6990)
        }
    },
    {
        'name': 'Desserts',
        'products': {
            '17': ('Café helado', 4990),
            '18': ('Cheesecake maracuyá', 3990),
            '19': ('Celestino', 3990),
            '20': ('Kuchen frutos rojos', 4500),
            '21': ('Torta Bailey´s', 4990)
        }
    }
]

tax_percentage = 0.08  #Impuesto del 8% solicitado según la rúbrica.-


# Ejecución del programa
def restaurant_management():
    global_total = 0    # Variable que almacena el total de ventas del día.
    tables = {}         # Diccionario vacío que registra el nº de mesas atendidas y sus detalles.
    max_tables = 15     # Número máximo de mesas en el restaurante.
    max_diner = 4       # Número máximo de comensales por mesa.

    tips = {1: '10%', 2: '15%', 3: '20%', 4: '25%'}   # Diccionario con opciones de propina.

    #Bucle que permite que el programa se siga ejecutando si están dentro de rango y no atendidas.-
    while len(tables) < max_tables:
        #Validación del número de mesa (entre 1 y 15 y no atendida/ocupada).-
        while True:
            table_number = input(f'\nIngrese un número de mesa entre 1 y {max_tables}: ')
            if validate_table_number(table_number, tables, max_tables):
                break  #Rompe ciclo si pasa la validación.-

        #Validación del nº de comensales por mesa.-
        while True:
            try:
                number_diners = int(input(f'Ingrese número de comensales para la mesa {table_number} (1-4): '))
                if 1 <= number_diners <= max_diner:
                    break  #Rompe bucle si pasa la validación.-
                else:
                    print(f'El número de comensales debe estar entre 1 y {max_diner}.')
            except ValueError:
                print('Debe ingresar un número válido.')

        diner_list = []  #Lista que almacena los detalles de los comensales.-
        total_table = 0  #Total de la mesa sin tax.-

        #Bucle que toma los pedidos de cada comensal (1 a 4).-
        for i in range(number_diners):
            print(f'\nTomar pedido comensal {i + 1}:')
            selected_items, total_diner = enter_order(cartas)
            diner_list.append({'comensal': i + 1, 'articulos': selected_items, 'total_diner': total_diner})
            total_table += total_diner  #Suma el total de cada comensal al total de la mesa.-

        #Cálculo tips y el total con tax.-
        tips_value = suggested_tip_calculator(total_table)
        total_table_with_tax = total_table * (1 + tax_percentage)
        final_total = total_table_with_tax + tips_value

        #Almacenamiento de la información de la mesa en el diccionario 'tables'.-
        tables[table_number] = {
            'total': total_table_with_tax,
            'tips': tips_value,
            'diners_detail': diner_list
        }

        global_total += final_total  #Acumula y almacena el total final de la mesa.-

        while True:
            respuesta = input('\n¿Desea atender otra mesa? (s/n): ').lower()
            if respuesta == 'n':
                break  #Rompe ciclo si el usuario ya no desea tomar más pedidos.-
            elif respuesta == 's':
                break  #Ingreso de otro pedido/reinicia el bucle.-
            else:
                print('Entrada inválida. Por favor ingrese "s" para sí o "n" para no.')

        if respuesta == 'n':
            break  #Si se han atendido todas las mesas, termina el ciclo principal.-

    #Impresión de los detalles de todas las mesas atendidas durante el día.-
    print_all_tables_details(tables)
    #Impresión del resumen de las ganancias del día.-
    print_daily_summary(tables)

#Declaración de función que permite imprimir en pantalla el detalle de cada mesa.-
def print_all_tables_details(tables):
    print('\n********** MESAS ATENDIDAS **********')  #Imprime detalle de todas las mesas.-

    #Bucle que itera el diccionario 'tables' que contiene la información de cada mesa.-
    for table_number, datos in tables.items():
        print(f'\nMesa nº {table_number}:')  #Imprime el número de la mesa.-
        print('Detalles de los comensales:')  #Imprime encabezado de los detalles de los comensales.-

        #Bucle que itera sobre la lista 'diners_detail' de cada mesa y muestra los detalles de cada comensal.-
        for comensal in datos['diners_detail']:
            print(f'  Comensal {comensal["comensal"]}:')  #Imprime el nombre del comensal.-
            print(f'    Artículos: {", ".join(comensal["articulos"])}')  #Imprime los artículos comprados.-
            print(f'    Total antes de impuestos: ${comensal["total_diner"]:,.0f}')  # Imprime el total sin impuestos del comensal.-

        #Impresión de los totales de la mesa.-
        print(f'Total con impuestos: ${datos["total"]:,.0f}')  #Imprime total con impuestos.-
        print(f'Propina total: ${datos["tips"]:,.0f}')  #Imprime propina total.-

#Declaración de función que permite imprimir el total de las ganancias del día.-
def print_daily_summary(tables):
    #Inicialización totales globales (contador en 0).-
    global_total = 0
    global_tips = 0

    #Cálculo del total global y tax.-
    for datos in tables.values():
        global_total += datos["total"]
        global_tips += datos["tips"]

    print('\n******** RESUMEN GANANCIAS DEL DÍA ********')  #Imprime resumen de las ganancias del día.-
    print(f'Total diario sin impuestos: ${global_total:,.0f}')  #Total sin impuestos.-
    print(f'Total diario con impuestos: ${global_total * (1 + tax_percentage):,.0f}')  # Total con impuestos.-
    print(f'Propina total: ${global_tips:,.0f}')  #Imprime total de propinas.-
    print(f'    \nTotal general del día con impuestos y propinas: ${global_total + global_tips:,.0f}')  #Total general con impuestos y propinas.-

    print('\n¡Gracias por utilizar el sistema de gestión de Pearl´s Pancake Pad!')
    print('               PROGRAMA CREADO POR MVMD')



# Ejecutar la gestión del restaurante
restaurant_management()