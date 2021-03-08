
nombreRestaurante = ''
categoriaActual = ''
errores = []
lexemas = []
factura = []
matrizArticulos = []

def agregarCategoria(categoria): # si no existe agrega una nueva si si no hace nada
    cate = False
    for i in matrizArticulos:
        if i[0] == categoria:
            cate = True
    if cate == False:
        matrizArticulos.append([categoria])
    
def agregarArticulo(articulo): # agrega el diccionario del articulo a la lista tomando en cuenta la categoria que esta seleccionada
    for lista in matrizArticulos:
        if lista[0] == categoriaActual:
            lista.append(articulo)

def verificaId(id):
    idIgual = False
    for lista in matrizArticulos:
        for w in range(1,len(lista)):
            if lista[w]['ID'] == id:
                idIgual = True
    return idIgual

def automata(nombreArchivo):
    global nombreRestaurante
    global categoriaActual
    global errores
    global lexemas
    errores.clear()
    lexemas.clear()
    factura.clear()
    matrizArticulos.clear()
    errorActivo = False
    archivo = open(nombreArchivo,"r")
    fila=1
    auxiliar = ''
    identificado = ''
    nombre = ''
    precio = 00
    descripcion = ''
    while (True):
        state = 0
        linea = archivo.readline()
        x=0
        decimal = 2
        errorActivo = False
        while x < len(linea):
            actual = linea[x]
            if state == 0:
                if actual == '[':
                    state = 5
                    x=x+1
                elif actual == ']':
                    if errorActivo == False:
                        if verificaId(identificado) == True: #existe un id con el mismo nombre
                            a = dict(Fila=fila,Columna=2,Caracter=identificado,Descripcion='ID es el mismo que un articulo previamente ingresado')
                            errores.append(a)
                        else:
                            a = dict(ID=identificado,nombre=nombre,precio=precio,descripcion=descripcion)
                            agregarArticulo(a)            
                    x=x+1
                elif ord(actual) == 61:
                    x=x+1
                    state = 1
                elif ord(actual) >= 48 and ord(actual) <= 57 or actual=='.':  #numeros
                    x=x+1
                elif ord(actual)==95 or ord(actual)==44 or ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165:
                    x=x+1
                elif ord(actual) == 32:
                    x=x+1
                elif ord(actual) == 39 and fila != 1:
                    state = 3
                    x = x+1
                elif ord(actual) == 39 and fila == 1:
                    state = 15
                    x = x+1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido')
                    errores.append(a)
                    x=x+1
    ###########################################################################  
            elif state == 1: 
                if ord(actual) == 39:
                    state = 2
                    x = x+1
                elif ord(actual) == 32:
                    x = x+1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido')
                    errores.append(a)
                    x=x+1
    ###########################################################################  
            elif state == 2: #aqui agrega nombre de restaurante
                if ord(actual) == 39:
                    nombreRestaurante = auxiliar
                    auxiliar = ''
                    b = dict(Lexema=nombreRestaurante,Fila=fila,Columna=x+1,Token='Cadena')
                    lexemas.append(b)
                    x = x+1
                    state = 0
                elif actual == '\n':
                    x = x+1 
                else: 
                    auxiliar = auxiliar + actual
                    x = x + 1
    ###########################################################################
            elif state == 3: #encarga de crear las categorias de comida
                if ord(actual) == 32:
                    x=x+1                                    #Estado 3
                elif ord(actual) == 39:
                    state = 4
                    categoriaActual = auxiliar
                    agregarCategoria(auxiliar)
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Cadena')
                    lexemas.append(b)
                    auxiliar = ''
                    x=x+1
                elif actual == '\n':
                    x = x+1
                else:  #errror
                    auxiliar = auxiliar +actual
                    x=x+1       
    ############################################################################    
            elif state == 4: #verifica que esten los 2 punto despupes de categoria
                if ord(actual) == 58 :
                    state = 0
                    x=x+1
                elif ord(actual) == 32:
                    x=x+1 
                elif ord(actual) == 91:
                    a = dict(Fila=fila,Columna=x+1,Caracter='Nulo',Descripcion='Falta caracter asignacion')
                    errores.append(a)
                    auxiliar = ''
                    state = 0    
                elif actual == '\n':
                    x = x+1                       
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido entre categoria y :')
                    errores.append(a)
                    x=x+1
                    auxiliar = ''
                    state = 0
    ##############################################################################
            elif state == 5: #verifica que el id del producto sea correcto
                if ord(actual)==95 or ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165:
                    auxiliar = auxiliar + actual  
                    x=x+1
                elif  ord(actual) >= 48 and ord(actual) <= 57:
                    auxiliar = auxiliar + actual
                    x=x+1
                elif ord(actual) == 32:
                    x=x+1
                elif ord(actual)==59:      
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Identificador')
                    lexemas.append(b)
                    identificado = auxiliar
                    auxiliar = ''
                    state = 7
                    x = x + 1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Error en Id')
                    errores.append(a)
                    auxiliar = auxiliar + actual
                    
                    x=x+1
                    state = 6
    ############################################################################
            elif state == 6:     #Termina de agregar toda la palabra de id erronea
                if ord(actual)==59:
                    a = dict(Fila=fila,Columna=x+1,Caracter=auxiliar,Descripcion='Identificador Erroneo')
                    errores.append(a)
                    errorActivo = True 
                    state = 7
                    auxiliar = ''
                    x = x+1
                elif actual == '\n':
                    x = x+1
                else:
                    auxiliar = auxiliar + actual
                    x=x+1
    #############################################################################################
            elif state == 7: #   #Manda a agregar todos los valores a la cadena 
                if ord(actual)==32:
                    x=x+1
                elif ord(actual)==39:
                    x=x+1
                    state = 8
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracte Desconocido')
                    errores.append(a)
                    x=x+1
    #################################################################################
            elif state == 8: #agrega todos los caracteres de nombre
                if  ord(actual)==39:
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Cadena')
                    lexemas.append(b)
                    nombre = auxiliar
                    auxiliar = ''
                    state = 9
                    x=x+1
                else:
                    auxiliar = auxiliar + actual
                    x=x+1
    ###################################################################
            elif state == 9:  #verifica que no haya caracteres desconocidos para enviarlos al siguiente
                if ord(actual)==32:
                    x=x+1
                elif ord(actual)==59:
                    state = 10
                    x=x+1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido')
                    errores.append(a)
                    x=x+1
    ######################################################################################################3
            elif state == 10: #veficia que no haya datos desconocidos en numeros
                if ord(actual)==32:
                    x=x+1
                elif ord(actual) >= 48 and ord(actual) <= 57:
                    auxiliar = auxiliar + actual
                    x=x+1
                elif ord(actual) == 46:
                    auxiliar = auxiliar + actual
                    x=x+1
                    state = 11
                elif ord(actual) == 59:
                    auxiliar = auxiliar + '.00'
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Numero')
                    lexemas.append(b)
                    precio = auxiliar
                    auxiliar = ''
                    state = 13 # estaod para descripcion
                    x=x+1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido')
                    errores.append(a)
                    state = 12 # agregara todos los valores
                    auxiliar = auxiliar + actual
                    x=x+1
    ####################################################################33
            elif state == 11: #verifica que des pues del punto hayan unicamente 2 ceros
                if decimal == 2 and ord(actual) >= 48 and ord(actual) <= 57:
                    auxiliar = auxiliar + actual
                    decimal = decimal - 1 
                    x=x+1
                elif decimal == 1 and ord(actual) >= 48 and ord(actual) <= 57:
                    aux = linea[x+1]
                    if ord(aux) >=48 and ord(aux) <= 57:
                        if int(aux) > 4:
                            f = int(actual)+1
                            auxiliar = auxiliar + str(f)
                        else:
                            auxiliar = auxiliar + actual
                    else:
                        auxiliar = auxiliar + actual
                    decimal = decimal - 1
                    x=x+1
                elif ord(actual)==32:
                    x=x+1
                elif ord(actual)==59 and decimal ==2:
                    auxiliar = auxiliar + '00'
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Numero')
                    lexemas.append(b)
                    precio = auxiliar
                    auxiliar = ''
                    state = 13 # estaod para descripcion
                    x=x+1
                elif ord(actual)==59 and decimal ==1:
                    auxiliar = auxiliar + '0'
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Numero')
                    lexemas.append(b)
                    precio = auxiliar
                    auxiliar = ''
                    state = 13 # estaod para descripcion
                    x=x+1
                elif ord(actual)==59 and decimal ==0:
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Numero')
                    lexemas.append(b)
                    precio = auxiliar
                    auxiliar = ''
                    state = 13 # estaod para descripcion
                    x=x+1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido')
                    errores.append(a)
                    x=x+1
    #################################################################################3
            elif state == 12:  # agrega todos los valores hasta encontrar punto y coma
                if ord(actual)==59:
                        a = dict(Fila=fila,Columna=x+1,Caracter=auxiliar,Descripcion='Error en Precio')
                        errores.append(a)
                        errorActivo = True 
                        state = 13
                        auxiliar = ''
                        x = x + 1
                elif actual == '\n':
                    x = x+1
                else:
                    auxiliar = auxiliar + actual
                    x=x+1
    #######################################################################################
            elif state == 13: #verifica que no haya valores extraños antes de enviar a 14
                if ord(actual)==32:
                    x=x+1
                elif ord(actual)==39:
                    auxiliar = ''
                    state = 14
                    x=x+1
                elif actual == '\n':
                    x = x+1
                else:
                    a = dict(Fila=fila,Columna=x+1,Caracter=actual,Descripcion='Caracter Desconocido')
                    errores.append(a)
                    x=x+1
    ############################################################################################333333
            elif state == 14: #agrega todos los valores en cola
                if ord(actual)==39:
                    b = dict(Lexema=auxiliar,Fila=fila,Columna=x+1,Token='Cadena D')
                    lexemas.append(b)
                    descripcion = auxiliar
                    auxiliar = ''
                    state = 0
                    x=x+1
                else: 
                    auxiliar = auxiliar + actual
                    x=x+1
    #########################################################################3
            elif state  == 15:
                if ord(actual)==32 or ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165:
                    auxiliar = auxiliar + actual
                    x = x+1
                elif ord(actual) == 39:
                    factura.append(auxiliar)
                    state = 16
    ################################################################################
            elif state == 16:
                if ord(actual) >= 48 and ord(actual) <= 57 or ord(actual)== 45:
                    auxiliar = auxiliar + actual

        if not linea:
            break
        fila=fila+1
    archivo.close()
    return nombreRestaurante
