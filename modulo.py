# Crea un diccionario que representa una película con sus atributos principales
def crear_pelicula(nombre, genero, duracion, anio, clasificacion, hora, dia):
  p={}
  p['nombre']=nombre
  p['genero']=genero
  p['duracion']=duracion
  p['hora']=hora
  p['dia']=dia
  p['anio']=anio
  p['clasificacion']=clasificacion
  return p


# Busca una película por nombre exacto y retorna su diccionario si la encuentra
def encontrar_pelicula(nombre_pelicula: str, 
                       p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict:
    
    # Se agrupan todas las películas en una lista
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    # Se recorre cada película buscando coincidencia por nombre
    for peli in bd:
        if peli['nombre'] == nombre_pelicula:
            # Si encuentra, retorna el diccionario asociado a ese nombre
            return peli
    
    # Si no se encuentra, retorna nada
    return None
 

# Retorna la película con mayor duración
def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict: 
    
    # Se agrupan las películas
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    # Lista auxiliar con las duraciones
    lt = []
    
    # Se extraen las duraciones
    for i in range(len(bd)):
        lt.append(bd[i]['duracion'])
    
    # Se obtiene el índice de la duración máxima y se retorna la película correspondiente
    return bd[lt.index(max(lt))]


# Calcula la duración promedio de las películas y la retorna en formato horas:minutos
def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict: 
    
    # Se agrupan las películas
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    # Lista de duraciones
    l_promedio = []
    
    # Se almacenan las duraciones
    for i in range(len(bd)):
        l_promedio.append(bd[i]['duracion'])

    # Se calcula el promedio en minutos
    promedio = sum(l_promedio)/len(l_promedio)
    
    # Conversión a horas y minutos
    h = int(promedio//60)
    m = int(promedio%60)
    
    return str(h) + ":" + str(m)


# Retorna una lista de películas cuyo año es mayor o igual al indicado
def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict, anio: int) -> dict: 
    
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    resultado = []
    
    # Filtra por año
    for i in range(len(bd)):
       if bd[i]['anio'] >= anio:
           resultado.append(bd[i])
    
    return resultado


# Retorna películas que se proyectan en un día específico
def encontrar_dia( dia: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict: 
    
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    resultado = []
    
    # Filtra por día
    for i in range(len(bd)):
       if bd[i]['dia'] == dia:
           resultado.append(bd[i])
    
    return resultado


# Retorna películas que se proyectan a una hora específica
def encontrar_hora(hora: int, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict: 
    
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    resultado = []
    
    # Filtra por hora
    for i in range(len(bd)):
       if bd[i]['hora'] == hora:
           resultado.append(bd[i])
    
    return resultado


# Cuenta cuántas películas tienen clasificación 18+
def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict: 
    
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    contador = 0
    
    # Se cuentan las películas 18+
    for i in range(len(bd)):
       if bd[i]['clasificacion'] == '18+':
           contador = contador + 1
           
    return contador 


# Retorna la lista de películas con clasificación 18+
def peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict,
                       p6: dict, p7: dict, p8: dict, p9: dict, p10: dict,
                       p11: dict, p12: dict, p13: dict, p14: dict, p15: dict,
                       p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict: 
    
    bd = [p1, p2, p3, p4, p5,
          p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15,
          p16, p17, p18, p19, p20]
    
    resultado = []
    
    # Filtra películas 18+
    for i in range(len(bd)):
       if bd[i]['clasificacion'] == '18+':
           resultado.append(bd[i])
            
    return resultado


# Reagenda una película validando restricciones de horario y día
def reagendar_pelicula(pel: dict, nueva_hora: int, nuevo_dia: str, control_horario: bool) -> bool:
    
    # Si se activa el control, se aplican restricciones
    if control_horario == True:
        
        # Restricción para documentales
        if pel['genero'] == 'Documental':
            if nueva_hora >= 2200:
                print("\nNo es posible reproducir Documentales despues de las 10:00pm")
                return False
        
        # Restricción para dramas
        if pel['genero'] == 'Drama':
            if nuevo_dia == 'Viernes':
                print("\nNo es posible reproducir Dramas los Viernes")
                return False
        
        # Restricción general de horario entre semana
        if nuevo_dia != 'Sábado' and nuevo_dia != 'Domingo':
            if nueva_hora >= 2300 or nueva_hora <= 600:
                print("\nNo es posible programar películas en este horario")
                return False

    # Si pasa las validaciones, se actualiza la película
    pel['hora'] = nueva_hora
    pel['dia'] = nuevo_dia
    
    return True


# Determina si un invitado puede ver una película según edad, género y clasificación
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    
    genero = peli['genero']
    clasificacion = peli['clasificacion']
    
    # Mayores de edad pueden ver cualquier película
    if edad_invitado >= 18:
        return True
    
    # Menores de 10 solo pueden ver contenido familiar
    if edad_invitado <= 10:
        if 'Familiar' in genero:
            return True
        else:
            return False
    
    # Menores de 15 no pueden ver terror
    if edad_invitado < 15:
        if 'Terror' in genero:
            return False
    
    # Validación según clasificación
    if clasificacion == 'Todos':
        return True
    elif clasificacion == '7+':
        if edad_invitado >= 7:
            return True
        elif 'Documental' in genero:
            return False
        else:
            return autorizacion_padres
    elif clasificacion == '13+':
        if edad_invitado >= 13:
            return True
        elif 'Documental' in genero:
            return False
        else:
            return autorizacion_padres
    elif clasificacion == '18+':
        return False
    
    return False