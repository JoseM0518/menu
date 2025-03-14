# Lista que almacena las notas
notas = []

# Función principal que maneja el menú
def notase():
    # Imprime el menú de opciones
    opciones = print("""
    Bienvenido al Menú de notas
    1. Agregar notas
    2. Editar notas
    3. Ver notas
    4. Salir
    """)
    
    # Solicita la opción que desea elegir el usuario
    op = int(input("Ingrese la opción que desea realizar: "))
    
    # Opción 1: Agregar notas
    if op == 1: 
        def agregarNota():
            # Solicita el número de notas que se desean agregar
            nnotas = int(input("Ingrese el número de notas que desea agregar: "))
            # Itera según el número de notas que desea agregar
            for i in range(nnotas): 
                # Pide la nota y la agrega a la lista de notas
                nota = float(input("Ingrese la nota: "))
                notas.append(nota)
        
        # Llama a la función para agregar las notas
        agregarNota()
        # Vuelve a mostrar el menú después de agregar las notas
        notase()
    
    # Opción 2: Editar notas
    elif op == 2:
        def editarNota():
            # Muestra la primera nota de la lista para hacer referencia
            print(f"Empezando desde 0 = ", notas[0])
            # Muestra todas las notas en la lista
            print(notas)
            # Solicita la posición de la nota que se quiere cambiar
            ncambiar = int(input("Ingrese el número de la nota que desea cambiar: "))
            # Cambia la nota en la posición seleccionada
            notas[ncambiar] = float(input("Ingrese la nueva nota: "))
            # Informa que las notas han sido actualizadas
            print("Notas actualizadas")
        
        # Llama a la función para editar una nota
        editarNota()
        # Vuelve a mostrar el menú después de editar las notas
        notase()
    
    # Opción 3: Ver notas
    elif op == 3:
        def verNota():
            # Muestra todas las notas de la lista
            print(f"Las notas son: ", notas)
        
        # Llama a la función para ver las notas
        verNota()
        # Vuelve a mostrar el menú después de ver las notas
        notase()
    
    # Opción 4: Salir
    elif op == 4:   
        # Mensaje de despedida y finaliza el programa
        print("Gracias por utilizar el programa")
        None
    
    # Si la opción ingresada no es válida
    else:
        # Muestra un mensaje de error y vuelve a mostrar el menú
        print("Opción no válida, por favor intente de nuevo")
        notase()

# Llama a la función notase() para ejecutar el programa
notase()
