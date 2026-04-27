# Proyecto-Peliculas
# 🎬 Mi Agenda de Películas

## Integrantes
- Jairo Alejandro Pulido Corrales
- Alessandro de Jesus Rivero Bracho

## Descripción
Aplicación de consola desarrollada en Python que permite administrar
una agenda de películas de una plataforma de streaming. El usuario
puede consultar información, reagendar películas y verificar si un
invitado puede asistir según su edad y las restricciones definidas.

## Estructura del proyecto
El proyecto está dividido en dos archivos principales:

### consola.py
Contiene la interfaz de usuario por consola. Presenta un menú
interactivo con validaciones de entrada y mensajes claros para
que el usuario entienda cada acción y su resultado.

### modulo.py
Contiene toda la lógica del negocio a través de las siguientes funciones:

- **crear_pelicula()**: Construye y retorna el diccionario con la
  información de una película (nombre, género, duración, año,
  clasificación, hora y día).

- **encontrar_pelicula()**: Busca una película por nombre entre
  las registradas y retorna su diccionario.

- **encontrar_pelicula_mas_larga()**: Recorre todas las películas
  y retorna la de mayor duración.

- **duracion_promedio_peliculas()**: Calcula el promedio de duración
  de todas las películas y lo retorna en formato HH:MM.

- **encontrar_estrenos()**: Lista las películas estrenadas después
  de un año dado por el usuario.

- **cuantas_peliculas_18_mas()**: Cuenta y retorna cuántas películas
  tienen clasificación 18+.

- **reagendar_pelicula()**: Modifica el día y la hora de una película
  validando conflictos de horario y reglas como:
  - No programar documentales después de las 10:00 p.m.
  - No programar dramas los viernes.
  - Entre semana no programar películas después de las 11:00 p.m.
    ni antes de las 6:00 a.m.

- **decidir_invitar()**: Determina si un invitado puede ver una
  película según su edad, el género y la autorización de los padres:
  - Mayores de 18 pueden ver cualquier película.
  - Menores de 10 solo pueden ver películas de género familiar.
  - Menores de 15 no pueden ver películas de terror.
  - Si no cumple la clasificación, se requiere autorización de padres
    excepto en documentales.

## Cómo ejecutar
1. Tener Python instalado (versión 3.x)
2. Tener ambos archivos en la misma carpeta
3. Ejecutar el archivo consola.py desde la terminal:
