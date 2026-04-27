import modulo as mod

salir = 0 #Variable en 0 para permanecer en la interfaz
consulta_consulta = 1 #Variable que permite reintentar opciones mientras esté en 1
peli1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
peli2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")
peli3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Dómingo")
peli4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
peli5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")
peli6 = mod.crear_pelicula("Batman", "Acción, Drama", 152, 2008, '13+', 2100, "Viernes")
peli7 = mod.crear_pelicula("Interstellar", "Ciencia-Ficción, Drama", 169, 2014, '13+', 1930, "Sábado")
peli8 = mod.crear_pelicula("Parasite", "Drama, Suspenso", 132, 2019, '18+', 2200, "Domingo")
peli9 = mod.crear_pelicula("Matrix", "Acción, Ciencia-Ficción", 136, 1999, '13+', 2000, "Lunes")
peli10 = mod.crear_pelicula("Titanic", "Romance, Drama", 195, 1997, '13+', 1830, "Martes")
peli11 = mod.crear_pelicula("Gladiator", "Acción, Drama", 155, 2000, '13+', 2100, "Miércoles")
peli12 = mod.crear_pelicula("Avengers", "Acción, Ciencia-Ficción", 181, 2019, '13+', 1700, "Jueves")
peli13 = mod.crear_pelicula("Coco", "Familiar, Animación", 105, 2017, 'Todos', 1500, "Viernes")
peli14 = mod.crear_pelicula("Joker", "Drama, Suspenso", 122, 2019, '18+', 2230, "Sábado")
peli15 = mod.crear_pelicula("Toy Story", "Familiar, Animación", 81, 1995, 'Todos', 1600, "Domingo")
peli16 = mod.crear_pelicula("Forrest Gump", "Drama, Comedia", 142, 1994, '13+', 1900, "Lunes")
peli17 = mod.crear_pelicula("El Rey Leon", "Familiar, Animación", 88, 1994, 'Todos', 1700, "Martes")
peli18 = mod.crear_pelicula("Pulp Fiction", "Drama, Crimen", 154, 1994, '18+', 2300, "Miércoles")
peli19 = mod.crear_pelicula("La La Land", "Romance, Musical", 128, 2016, '13+', 2000, "Jueves")
peli20 = mod.crear_pelicula("The Godfather", "Drama, Crimen", 175, 1972, '18+', 2100, "Viernes")


total_peliculas = [
    peli1, peli2, peli3, peli4, peli5,
    peli6, peli7, peli8, peli9, peli10,
    peli11, peli12, peli13, peli14, peli15,
    peli16, peli17, peli18, peli19, peli20
] #lista de peliculas


while salir == 0:
    while True:    #Permanece en true porque en la linea 57 hay un break que detiene el loop
        print("=" * 52)
        print("|     🎬       - MENU PRINCIPAL -                  |")
        print("=" * 52)
        print("|" + " " * 50 + "|")
        print("|  [1]  Consultar pelicula por nombre          |")
        print("|  [2]  Consultar pelicula mas larga           |")
        print("|  [3]  Duracion promedio de peliculas         |")
        print("|  [4]  Consultar estrenos de un año           |")
        print("|  [5]  Peliculas con clasificacion +18        |")
        print("|  [6]  Reagendar una pelicula                 |")
        print("|  [7]  Verificar si puedes invitar a alguien  |")
        print("|  [8]  Salir de la aplicacion                 |")
        print("|" + " " * 50 + "|")
        print("=" * 50)

        entrada = input("\n  >> Seleccione una opcion: ")

        if entrada.isdigit() and (int(entrada) <= 8): 
            decision_menu = int(entrada)
            consulta_consulta = 1
            break
        else:
            print("  Ingrese un numero entre 1 y 8")
    
    
    
    if decision_menu == 1:
        print("\n--------------------------BUSCAR PELÍCULA--------------------------")
        while consulta_consulta == 1: 
            
            encontrar_nombre = input("\nIngrese el nombre de la pelicula con cada inicial en mayuscula: ")
            resultado = mod.encontrar_pelicula(encontrar_nombre, peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10,peli11, peli12, peli13, peli14, peli15,peli16, peli17, peli18, peli19, peli20)
            
            # Muestra el resultado asociado al nombre ingresado
            if resultado:
                print(f"\n--------------------------{resultado['nombre']}--------------------------")
                print (f"\n🌟 Nombre: {resultado['nombre']}")
                print (f"   Genero: {resultado['genero']}")
                h = resultado['duracion'] // 60
                m = resultado['duracion'] % 60
                print("   Duración:", str(h) + ":" + str(m))
                print (f"   Año de lanzamiento: {resultado['anio']}")
                print (f"   Clasificación: {resultado['clasificacion']}")
                print (f"   Hora y dia de reproducción: {resultado['hora']} || {resultado['dia']} ")
                print("\nDesea encontrar otra pelicula?")
                print("⚪ Digite 0 para volver al menú")
                print("✨ Digite 1 para consultar de nuevo")
                consulta_consulta = (input("Inserte su respuesta: "))
                if consulta_consulta == "1":
                    consulta_consulta = 1
                
                #Si el estado de consulta cambia (o sea, se ingresa 0) o algun valor errado, se regresa al menú
                elif consulta_consulta == "0":
                    consulta_consulta = 0
                else:
                    print("\nCaracter no valido, Volviendo al menu...")
                    consulta_consulta = 0
            else:
                print("No se encontró la película, intentelo de nuevo")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    if decision_menu == 2:
        
        resultado = mod.encontrar_pelicula_mas_larga(peli1, peli2, peli3, peli4, peli5,peli6, peli7, peli8, peli9, peli10,peli11, peli12, peli13, peli14, peli15,peli16, peli17, peli18, peli19, peli20)
        
        print("\n--------------------------PELÍCULA MÁS LARGA--------------------------\n")

        print(f"\nNombre: {resultado['nombre']}")
        print(f"Género: {resultado['genero']}")
        h = resultado['duracion'] // 60
        m = resultado['duracion'] % 60
        print("Duración:", str(h) + ":" + str(m))
        print(f"Año: {resultado['anio']}")
        print(f"Clasificación: {resultado['clasificacion']}")
        print(f"Horario: {resultado['hora']} - {resultado['dia']}\n")
        enter = (input("Presione enter para volver al menú: "))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    if decision_menu == 3:
    
        print("\nEn promedio, las películas duran: ⌚", mod.duracion_promedio_peliculas(peli1, peli2, peli3, peli4, peli5,peli6, peli7, peli8, peli9, peli10,peli11, peli12, peli13, peli14, peli15,peli16, peli17, peli18, peli19, peli20))
        enter = (input("Presione enter para volver al menú: "))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    if decision_menu == 4:
        while consulta_consulta == 1:
            consulta_estreno = int(input("\nInserte el año de estreno (ejem: 2004): "))
            resultado = mod.encontrar_estrenos(peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10,peli11, peli12, peli13, peli14, peli15,peli16, peli17, peli18, peli19, peli20, consulta_estreno)

            if resultado:   # muestra los estrenos solo entra si hay coincidencias en el año ingresado o estrenos despues de este
                print(f"\n-----------------------PELÍCULAS EN ESTRENO DESPUÉS DEL AÑO {consulta_estreno}-------------------------\n")
                for peli in resultado:
                    print("    ")
                    print("    ")
                    print("👲Nombre: ", peli['nombre'])
                    print("🥁Género: ", peli['genero'])
                    h = peli['duracion'] // 60
                    m = peli['duracion'] % 60
                    print("  Duración:", f"{h}:{m}")
                    print("  Año: ", peli['anio'])
                    print("👤Clasificación: ", peli['clasificacion'])
                    print(f"  Horario: {peli['hora']} - {peli['dia']}")
                    print("--" *50)
                    print("    ")
                    
                print("\nDesea encontrar otras fechas de estreno?")
                print("🌟⚪ Digite 0 para volver al menú")
                print("🌟✨ Digite 1 para consultar de nuevo")
                consulta_consulta = int(input("Inserte su respuesta: "))
                if consulta_consulta == 0:
                    consulta_consulta = 0
                elif consulta_consulta == 1:
                    consulta_consulta = 1
                else:
                    print("\nCaracter no valido, Volviendo al menu...")
                    consulta_consulta = 0
            else:
                print("No se encontró el estreno, intentelo de nuevo")
                



































    if decision_menu == 5:
        
        pelis_mas18 = mod.cuantas_peliculas_18_mas(peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10,peli11, peli12, peli13, peli14, peli15,peli16, peli17, peli18, peli19, peli20)
        resultado = mod.peliculas_18_mas(peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10,peli11, peli12, peli13, peli14, peli15,peli16, peli17, peli18, peli19, peli20)
        print("\n----------------------PELÍCULAS SOLO PARA ADULTOS-----------------------")
        
        # Primero, muestra cuantas peliculas +18 hay
        print("\nLa App le ofrece", pelis_mas18, "películas +18")
        
        # Luego, cuales son esas películas
        for peli in resultado:
            
            print("\n🔞Nombre: ",peli['nombre'])
            print("👤Género: ",peli['genero'])
            h = peli['duracion'] // 60
            m = peli['duracion'] % 60
            print("  Duración:", str(h) + ":" + str(m))
            print("  Año: ",peli['anio'])
            print("  Clasificación: ",peli['clasificacion'])
            print(f" Horario: {peli['hora']} - {peli['dia']}")
        print("")
        enter = (input("Inserte enter para volver al menú "))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if decision_menu == 6:
        print("\n--------------------------REPROGRAMAR PELÍCULA--------------------------")
        nombre = input("\nIngrese el nombre de la película (ejem: Shrek): ")
        
        #Primero, busca la pelicula que se desea reagendar
        resultado = mod.encontrar_pelicula(nombre, peli1, peli2, peli3, peli4, peli5,
                           peli6, peli7, peli8, peli9, peli10,
                           peli11, peli12, peli13, peli14, peli15,
                           peli16, peli17, peli18, peli19, peli20)
        if resultado:
            
            # Segundo, Ingresa lo datos de reagendamiento
            nuevo_dia = input("Inserte el nuevo día (ejem: Lunes): ")
            nueva_hora = int(input("Inserte la nueva hora (ejem: 1400 para 2pm): "))

            resultado_hora = mod.encontrar_hora(nueva_hora, peli1, peli2, peli3, peli4, peli5,
                           peli6, peli7, peli8, peli9, peli10,
                           peli11, peli12, peli13, peli14, peli15,
                           peli16, peli17, peli18, peli19, peli20)
            
            # Si los datos ingresados se encuentran con otra película programada en ese mismo horario, se cancela el reagendamiento
            if resultado_hora:
                print("No se puede programar: la hora ya está ocupada por otra película.❌")
                
            # Si estos no coinciden con un horario ya asignado, Verifica si el usuario esta seguro de reagendar
            else:
                print("\n¿Está seguro de su reprogramación?")
                print("1. SI")
                print("0. NO")
                seguro = int(input("Seleccione: "))
                
                # Por ultimo, si el usuario confirma, se reagenda en el horario (si pasa todos los filtros)
                if seguro == 1:
                    exito = mod.reagendar_pelicula(resultado, nueva_hora, nuevo_dia, True)
                    if exito:
                        print("✅¡Película reprogramada exitosamente!")
                        
                # Si no confirma, se cancela la reprogramación
                else:
                    print("Reprogramación cancelada. ❌")
        else:
            print("Película no encontrada. ❌")
                
         
         
         
         
         
         
         
         
         
         
         
    if decision_menu == 7:

        print("\n" + "=" * 52)
        print("|" + " VERIFICAR INVITADO ".center(50) + "|")
        print("=" * 52)
    
        # Primero, se solicita el nombre de la película a evaluar
        nombre_peli = input("\nIngrese el nombre de la pelicula: ")
        resultado = mod.encontrar_pelicula(nombre_peli, peli1, peli2, peli3, peli4, peli5,
                                       peli6, peli7, peli8, peli9, peli10, peli11, peli12,
                                       peli13, peli14, peli15, peli16, peli17, peli18,
                                       peli19, peli20)
        
        # Segundo, se verifica si la película existe
        if resultado:
            
            # Luego, se solicita la edad del invitado
            entrada_edad = input("Ingrese la edad del invitado: ")
    
            # Valida si la edad es un numero
            if entrada_edad.isdigit():
                edad = int(entrada_edad)
    
                # Se pregunta si el invitado tiene autorización de sus padres
                print("\nEl invitado tiene autorizacion de sus padres?")
                print("  1 Si")
                print("  0 No")
                entrada = input("\n  >> Digite su respuesta: ")
    
                # Conversión de la entrada a valor booleano
                if entrada == "1":
                    autorizacion = True
                elif entrada == "0":
                    autorizacion = False
                else:
                    # Si el valor no es válido, se asume sin autorización
                    print("\nCaracter no valido, volviendo al menu...")
                    autorizacion = False
    
                # Se evalúa si el invitado puede ver la película según reglas del sistema
                puede = mod.decidir_invitar(resultado, edad, autorizacion)
    
                # Por ultimo, muestra el resultado final de la validación
                if puede:
                    print("\nEl invitado SI puede ver la pelicula " + resultado['nombre'])
                else:
                    print("\nEl invitado NO puede ver la pelicula " + resultado['nombre'])
                    
                    # Se muestra la clasificación requerida como información adicional
                    print("Clasificacion requerida: " + resultado['clasificacion'])
    
            else:
                # Si la edad no es válida, se cancela la operación
                print("\nEdad no valida, volviendo al menu...")
        
        else:
            # Si la película no existe, se informa al usuario
            print("\nPelicula no encontrada, volviendo al menu...")
        
        # Pausa antes de regresar al menú principal
        input("\n  >> Presione Enter para volver al menu: ")
         
         
         
         
         
         
         
         
         
         
                
    if decision_menu == 8:
        
        print("\n                        Saliendo de la aplicación...")
        salir = 1
        break