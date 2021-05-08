from tinderish import *
from os import remove

# Test de la funcion que asigna una categoria a cada edad
def test_rangoDeEdad():
    # Se leen del archivo de entrada una lista de numeros (un numero por linea) que seran convertidos a rangos de edades usando la funcion rangoDeEdad
    # Luego se comparan con los rangos esperados para cada numero, los cuales se encuentran en el archivo de salida
    archivoEntrada = open("testRangoEdadEntrada.txt")
    edadesComoString = archivoEntrada.read().split("\n")
    archivoSalida = open("testRangoEdadSalida.txt")
    categoriasEnOrden = archivoSalida.read().split("\n")
    cantidadPruebas = len(edadesComoString)
    indice = 0
    while indice < cantidadPruebas:
        assert rangoDeEdad(int(edadesComoString[indice])) == categoriasEnOrden[indice]
        indice += 1

# Test de la funcion inicial que lee el archivo de personas
# y genera el diccionario
def test_leerPersonas():
    # Se lee un archivo de entrada con personas (mismo formato que ejemplos en campus) y un archivo con la salida esperada
    # El archivo de salida contiene una representación del diccionario esperado como string
    # Podemos convertir este string de vuelta a un diccionario utilizando la funcion 'eval'
    # Despues de hacer esto, generamos el diccionario con la funcion utilizada en el programa y comparamos los dos diccionarios

    inputFileName = "testPersonasLeerPersonas.txt"
    outputFileNameSolteros = "outputTestLeerPersonas.txt"

    archivoRespuestaDiccionario = open("testDiccionarioEsperado.txt", "r")
    diccionarioEsperado = eval(archivoRespuestaDiccionario.read())
    archivoRespuestaDiccionario.close()

    archivoRespuestaSolteros = open("testSolterosLeerPersonas.txt", "r")
    lecturaEsperada = archivoRespuestaSolteros.read()
    archivoRespuestaSolteros.close()


    assert leerPersonasYGenerarArchivoSolterosInicial(inputFileName, outputFileNameSolteros) == diccionarioEsperado

    archivo = open(outputFileNameSolteros)
    assert archivo.read() == lecturaEsperada

    archivo.close()
    remove(outputFileNameSolteros)

# Test de la funcion que se encarga de emparejar 
# las personas de una misma lista
def test_emparejarIguales():
    # Se realiza un procedimiento similar a los anteriores.
    # Se leen archivos de entrada con listas de personas (mismo formato que ejemplos) y se intentan emparejar entre sí
    # Luego se compara la lista de resultados con un archivo que contiene la salida esperada
    archivo = open("testEscribirParejasEmparejarIguales.txt", "w+")
    archivoPersonas = open("testEmparejarIgualesPersonas1.txt", "r")
    personas = archivoPersonas.read().split('\n')
    archivoPersonas.close()
    listaPersonas1 = []
    for persona in personas:
        datos = persona.split(",")
        personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
        listaPersonas1.append(personita)

    archivoPersonas = open("testEmparejarIgualesPersonas2.txt", "r")
    personas = archivoPersonas.read().split('\n')
    archivoPersonas.close()
    listaPersonas2 = []
    for persona in personas:
        datos = persona.split(",")
        personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
        listaPersonas2.append(personita)

    archivoRestantes = open("testRestantesEmparejarIguales1.txt", "r")
    personas = archivoRestantes.read().split('\n')
    archivoRestantes.close()
    listaRestantes1 = []
    for persona in personas:
        datos = persona.split(",")
        personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
        listaRestantes1.append(personita)
    
    archivoRestantes = open("testRestantesEmparejarIguales2.txt", "r")
    personas = archivoRestantes.read().split('\n')
    archivoRestantes.close()
    listaRestantes2 = []
    for persona in personas:
        datos = persona.split(",")
        personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
        listaRestantes2.append(personita)

    assert emparejarIguales(listaPersonas1, archivo) == listaRestantes1
    assert emparejarIguales(listaPersonas2, archivo) == listaRestantes2
    archivo.close()
    archivo = open("testEscribirParejasEmparejarIguales.txt")
    archivoRespuesta = open("testParejasEmparejarIgualesRespuesta.txt")
    assert archivo.read() == archivoRespuesta.read()
    archivo.close()
    archivoRespuesta.close()
    remove("testEscribirParejasEmparejarIguales.txt")

# Test de la funcion que se encarga de emparejar 
# las personas entre dos listas
def test_emparejarDistintos():
    # Se leen de dos archivos dos listas de personas y se las intenta emparejar
    # (para diferenciar las listas distintas en el mismo archivo las separamos con un renglon en blanco
    # es decir, el formato de archivo de entrada es el mismo que ejemplo pero con un enter que separa dos entradas)
    # El resultado se compara con un archivo que contiene la salida esperada
    # Las personas que no se pudieron emparejar se comparan con otro archivo de control que contiene los solteros esperados
    archivo = open("testEscribirParejasEmparejarDistintos.txt", "w+")
    archivoPersonas = open("testEmparejarDistintosPersonas1.txt", "r")
    personas = archivoPersonas.read().split('\n')
    archivoPersonas.close()
    listaPersonas1 = []
    listaPersonas2 = []
    cambioLista = False
    for persona in personas:
        if (persona == ""):
            cambioLista = True
        datos = persona.split(",")
        if (len(datos) == 6):
            personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
            if(not cambioLista):
                listaPersonas1.append(personita)
            else:
                listaPersonas2.append(personita)

    archivoPersonas = open("testEmparejarDistintosPersonas2.txt", "r")
    personas = archivoPersonas.read().split('\n')
    archivoPersonas.close()
    listaPersonas3 = []
    listaPersonas4 = []
    cambioLista = False
    for persona in personas:
        if (persona == ""):
            cambioLista = True
        datos = persona.split(",")
        if (len(datos) == 6):
            personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
            if (not cambioLista):
                listaPersonas3.append(personita)
            else:
                listaPersonas4.append(personita)
        
    archivoPersonas = open("testRestantesEmparejarDistintosPersonas1.txt", "r")
    personas = archivoPersonas.read().split('\n')
    archivoPersonas.close()
    restantesEsperadosPersonas1Lista1 = []
    restantesEsperadosPersonas1Lista2 = []
    cambioLista = False
    for persona in personas:
        if (persona == ""):
            cambioLista = True
        datos = persona.split(",")
        if (len(datos) == 6):
            personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
            if (not cambioLista):
                restantesEsperadosPersonas1Lista1.append(personita)
            else:
                restantesEsperadosPersonas1Lista2.append(personita)


    archivoPersonas = open("testRestantesEmparejarDistintosPersonas2.txt", "r")
    personas = archivoPersonas.read().split('\n')
    archivoPersonas.close()
    restantesEsperadosPersonas2Lista1 = []
    restantesEsperadosPersonas2Lista2 = []
    cambioLista = False
    for persona in personas:
        if (persona == ""):
            cambioLista = True
        datos = persona.split(",")
        if (len(datos) == 6):
            personita = (datos[0].strip(), datos[1].strip(), datos[2].strip(), int(datos[3].strip()), datos[4].strip(), datos[5].strip())
            if (not cambioLista):
                restantesEsperadosPersonas2Lista1.append(personita)
            else:
                restantesEsperadosPersonas2Lista2.append(personita)

    archivoRespuesta = open("testEmparejarDistintosEscrituraEsperada.txt")

    assert emparejarDistintos(listaPersonas1, listaPersonas2, archivo) == (restantesEsperadosPersonas1Lista1, restantesEsperadosPersonas1Lista2)
    assert emparejarDistintos(listaPersonas3, listaPersonas4, archivo) == (restantesEsperadosPersonas2Lista1, restantesEsperadosPersonas2Lista2)

    archivo.close()
    archivo = open("testEscribirParejasEmparejarDistintos.txt")
    assert archivo.read() == archivoRespuesta.read()
    archivo.close()
    archivoRespuesta.close()
    remove("testEscribirParejasEmparejarDistintos.txt")
