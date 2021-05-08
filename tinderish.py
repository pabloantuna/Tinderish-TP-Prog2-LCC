####################################################
##                Programacion II                 ##
##              Trabajo Practico I                ##
## Integrantes: Antuña, Pablo - Garavano, Lautaro ##
####################################################

### INICIO REPRESENTACION DE DATOS ###

# Las personas en este programa son representadas como una tupla que contiene
# como datos: nombre, apellido, edad, localidad, genero, genero de interes

# 0 nombre
# 1 apellido
# 2 localidad
# 3 edad
# 4 genero
# 5 genero de interes


# Decidimos crear una estructura que separe las personas en base a su localidad, su edad, su interes, y su genero.
# Mas precisamente, tendremos un diccionario cuyas keys son las distintas localidades, y los valores dentro de cada key
# seran otros diccionarios. En estos diccionarios, cada key representa la categoria en base a la edad que se asigna a cada persona.
# El valor dentro de cada key de categoria es a su vez otro diccionario cuyas keys seran el genero de interes de la persona (M, F o A)
# Dentro de esa key hay dos keys, una para genero masculino y otra para genero femenino. Dentro de estas ultimas
# habra una lista de tuplas que seria una lista de personas

### FIN REPRESENTACION DE DATOS ###

# Funcion que toma la edad de una persona y devuelve un string
# que representa su 'categoria'
def rangoDeEdad(edad):
    if edad >= 18:
        return "adulto"
    elif edad >= 15:
        return "adolescente"
    else:
        return "jovenAdolescente"

# Funcion que toma 2 strings que representan el nombre del archivo de entrada
# y el nombre del archivo de salida de los solteros, lee las personas y escribe
# en el ultimo archivo los solteros que ya podemos encontrar (edad<=10, asexual)
# devuelve un diccionario que contiene los datos leidos
def leerPersonasYGenerarArchivoSolterosInicial(inputFileName, outputFileNameSolteros):
    archivo = open(inputFileName, "r", encoding="latin1")
    archivoSolteros = open(outputFileNameSolteros, "w+")
    text = archivo.read()
    archivo.close()
    # Uso de la funcion split de strings para dividir el texto leido del archivo en distintas filas
    filas = text.split("\n")
    localidades = {}
    for fila in filas:
        # Uso de la funcion split de strings para dividir el texto leido en la fila en una lista con los datos de la persona
        datos = fila.split(",")
        persona = ()
        # Uso de la funcion len para asegurarme que estoy leyendo 6 datos (ya que puede haber una linea en blanco o ser otro formato que no trabajamos)
        if(len(datos) == 6):
            # Uso de la funcion strip de strings para eliminar espacios al inicio y al final del string leido
            persona = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
            if not (persona[5] == "N" or persona[3] <= 10):
                if persona[2] not in localidades.keys():
                    localidades[persona[2]] = {'jovenAdolescente': {'M': {'M': [], 'F': []} , 'F': {'M': [], 'F': []}, 'A': {'M': [], 'F': []}} , 'adolescente': {'M': {'M': [], 'F': []} , 'F': {'M': [], 'F': []}, 'A': {'M': [], 'F': []}}, 'adulto': {'M': {'M': [], 'F': []} , 'F': {'M': [], 'F': []}, 'A': {'M': [], 'F': []}}}
                # Uso de append para agregar la persona a la lista
                localidades[persona[2]][rangoDeEdad(persona[3])][persona[5]][persona[4]].append(persona)
            else:
                if (persona[3] <= 10 and persona[5] == "N"):
                    motivo = "MENOR DE EDAD Y ASEXUAL"
                elif (persona[3] <= 10):
                    motivo = "MENOR DE EDAD"
                else:
                    motivo = "ASEXUAL"
                linea = persona[0] + ', ' + persona[1] + ', ' + str(persona[3]) + ', ' + persona[2] + " - Motivo: " + motivo + '\n'
                archivoSolteros.write(linea)
    archivoSolteros.close()     
    return localidades

# Funcion que toma una lista de personas y el archivo (no el nombre)
# en el cual escribir las parejas que forma entre personas de esa misma lista
# escribe en el archivo pasado como argumento las parejas formadas
# devuelve la lista sin las personas que formaron pareja
def emparejarIguales(personas, archivoParejas):
    indice = 0
    indice2 = 1
    # Uso de la funcion len para obtener el largo de la lista
    largoLista = len(personas)
    while (indice < largoLista and indice2 < largoLista):
        linea = personas[indice][0] + ', ' + personas[indice][1] + ', ' + str(personas[indice][3]) + ' - ' + personas[indice2][0] + ', ' + personas[indice2][1] + ', ' + str(personas[indice2][3]) + ' - ' + personas[indice2][2] + '\n'
        archivoParejas.write(linea)
        indice += 2
        indice2 += 2

    # Como estoy emparejando entre personas de la misma lista, se que
    # emparejo a todos o me queda solo uno, dependiendo de si el largo es par o impar
    if (largoLista % 2 != 0):
        personasRestantes = [personas[-1]]
    else:
        personasRestantes = []

    return personasRestantes

# Funcion que toma dos listas de personas y el archivo (no el nombre)
# en el cual escribir las parejas que forma entre personas de las distintas listas
# escribe en el archivo pasado como argumento las parejas formadas
# devuelve una tupla con las listas sin las personas que formaron pareja
def emparejarDistintos(personas, personas2, archivoParejas):
    indice = 0
    # Uso de la funcion len para obtener el largo de las listas
    largoLista1 = len(personas)
    largoLista2 = len(personas2)
    while (indice < largoLista1 and indice < largoLista2):
        linea = personas[indice][0] + ', ' + personas[indice][1] + ', ' + str(personas[indice][3]) + ' - ' + personas2[indice][0] + ', ' + personas2[indice][1] + ', ' + str(personas2[indice][3]) + ' - ' + personas2[indice][2] + '\n'
        archivoParejas.write(linea)
        indice += 1
    personasRestantes =  personas[indice:]
    personas2Restantes =  personas2[indice:]

    return personasRestantes, personas2Restantes

# Funcion que toma un diccionario que represente a todas las personas
# y dos strings que representan los nombres de los archivos de salida de las parejas y de los solteros
# esta funcion se encarga de ir armando parejas y escribirlas en el archivo de salida de parejas
# tambien escribe los solteros que quedan y el motivo de por que quedan solteros en el archivo de salida de solteros
def escribirParejasEnArchivoYAgregarSolteros(diccionario, outputFileNameParejas, outputFileNameSolteros):
    archivoParejas = open(outputFileNameParejas, "w+")
    archivoSolteros = open(outputFileNameSolteros, "a+")

    # Recorreremos todos los valores del diccionario, en el que encontraremos subdiccionarios correspondientes a las diferentes localidades de las personas
    # Dentro de cada localidad emparejaremos a las personas con personas de esa localidad
    # Dado que una persona solo puede emparejarse con otra de la misma localidad, no habrá ninguna pareja que nos estemos salteando
    for localidad in diccionario.values():
        # Análogamente, una persona solo puede relacionarse con otra del mismo rango de edad, por lo que emparejaremos personas dentro de cada categoria por separado
        for categoria in localidad.values():
            # Primero emparejamos los heterosexuales
            categoria["M"]["F"], categoria["F"]["M"] = emparejarDistintos(categoria["M"]["F"], categoria["F"]["M"], archivoParejas)
            # Luego emparejamos los hombres homosexuales
            categoria["M"]["M"] = emparejarIguales(categoria["M"]["M"], archivoParejas)
            # Luego emparejamos las mujeres homosexuales
            categoria["F"]["F"] = emparejarIguales(categoria["F"]["F"], archivoParejas)
            # Luego usamos los bisexuales como "comodines" para completar con los que quedaron sin pareja
            categoria["F"]["M"], categoria["A"]["F"] =  emparejarDistintos(categoria["F"]["M"], categoria["A"]["F"], archivoParejas)

            categoria["M"]["F"], categoria["A"]["M"] =  emparejarDistintos(categoria["M"]["F"], categoria["A"]["M"], archivoParejas)
        
            categoria["F"]["F"], categoria["A"]["F"] =  emparejarDistintos(categoria["F"]["F"], categoria["A"]["F"], archivoParejas)

            categoria["M"]["M"], categoria["A"]["M"] =  emparejarDistintos(categoria["M"]["M"], categoria["A"]["M"], archivoParejas)
            # Luego emparejamos entre bisexuales
            categoria["A"]["F"], categoria["A"]["M"] =  emparejarDistintos(categoria["A"]["F"], categoria["A"]["M"], archivoParejas)
            # Por ultimo emparejamos los bisexuales del mismo genero entre si
            categoria["A"]["M"] = emparejarIguales(categoria["A"]["M"], archivoParejas)

            categoria["A"]["F"] = emparejarIguales(categoria["A"]["F"], archivoParejas)
            
            #Luego del emparejado, recorreremos las listas para escribir en el archivo las personas que quedaron sin pareja
            for generoDeInteres in categoria.values():
                for genero in generoDeInteres.values():
                    for soltero in genero:
                        linea = soltero[0] + ', ' + soltero[1] + ', ' + str(soltero[3]) + ', ' + soltero[2] + " - Motivo: NO QUEDARON PERSONAS COMPATIBLES" + '\n'
                        archivoSolteros.write(linea)

    archivoParejas.close()
    archivoSolteros.close()

# El siguiente bloque se ejecuta al iniciar el programa por consola
# para no necesitar llamar a las funciones por el interprete
if __name__ == "__main__":
    fileName = input("Ingrese nombre del archivo de entrada: ")
    diccionario = leerPersonasYGenerarArchivoSolterosInicial(fileName, "solteros.txt")
    escribirParejasEnArchivoYAgregarSolteros(diccionario, "parejasFormadas.txt", "solteros.txt")
