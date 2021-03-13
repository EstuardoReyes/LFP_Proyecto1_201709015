from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from Automata import automata
from Automata import nombreRestaurante,matrizArticulos,errores,lexemas,factura
import webbrowser
from datetime import datetime
from graphviz import Digraph


archivoMenu = ''
archivoOrden = ''
salida = False
archivo_Menu_Seleccionado = False
archivo_Orden_Seleccionado = False
name = ''


def cls():
    r=0
    while r<10:
        print("")
        r=r+1 

def cargaMenu():
    global archivoMenu
    global archivo_Menu_Seleccionado
    global name
    root = Tk()
    root.withdraw()
    matrizArticulos.clear()
    errores.clear()
    lexemas.clear()
    root.wm_attributes("-topmost", 1)
    archivoMenu = askopenfilename(initialdir="D:\Galeria\Escritorio",filetypes =(("Archivo LFP", "*.lfp"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()
    print("Archivo Menu seleccionada correctamente")
    archivo_Menu_Seleccionado = True
    name = automata(archivoMenu)
    mensaje =  """<!doctype html>
                        <html>
                        <head>
                        <title>LEXEMAS</title>
                        <link href="CSS\pa.css" rel="stylesheet" type="text/css">
                        </head>
                        <body>
                        <div class="container"> 
                        <header> <a href="">
                        <h6 class="logo">REPORTE</h6>
                        </a>
                        </header>
                        <section class="hero" id="hero">
                        <h3 class="hero_header">INFORME DE LEXEMAS</h3>
                        <p class="tagline">Menu</p>
                        </section>
                        <section class="banner">
                        <div style="text-align:center;">
                        <table  border=1 bordercolor="white" style="margin: 0 auto;bgcolor="#FFFFFF">
                        <tr>
                        <td><font color = "white">id</td><td><font color = "white">Lexemas</td><td><font color = "white">Fila</td><td><font color = "white">Columna</td><td><font color = "white">Token</td>
                        </tr>"""
    i = 1
    tamaño = 20
    for lexema in lexemas:    
        mensaje = mensaje + """<tr><td><font color = "white">"""+str(i)+"""</td><td><font color = "white">"""+lexema['Lexema']+"""</td><td><font color = "white">"""+str(lexema['Fila'])+"""</td><td><font color = "white">"""+str(lexema['Columna'])+"""</td><td><font color = "white">"""+lexema['Token']+"""</td></tr>"""
        i = i + 1
        tamaño = tamaño + 38
    mens =""" </table> </div> <div class="copyright">&copy;2020- <strong>Edwin estuardo reyes reyes</strong></div>
                        </div>
                        </body>
                        </html>"""
    mensaje = mensaje + mens


    css = """@charset "UTF-8";
                    /* Body */
                    html {
                            font-size: 30px;
                        }
                        body {
                            font-family: source-sans-pro;
                            background-color: #f2f2f2;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            font-style: normal;
                            font-weight: 200;
                            }
                            .container {
                            width: 70%;
                            margin-left: auto;
                            margin-right: auto;
                            height: 700px;
                                        }
                            header {
                            width: 100%;
                            height: 8%;
                            background-color: #52bad5;
                            border-bottom: 1px solid #2C9AB7;
                            }
                            .logo {
                        color: #fff;
                            font-weight: bold;
                            text-align: undefined;
                            width: 10%;
                            float: left;
                            margin-top: 15px;
                            margin-left: 25px;
                            letter-spacing: 4px;
                                }
                            .hero_header {
                            color: #FFFFFF;
                            text-align: center;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            letter-spacing: 4px;
                                }
                            .hero {
                            background-color: #B3B3B3;
                            padding-top: 100px;
                            padding-bottom: 80px;
                            }
                            .light {
                                font-weight: bold;
                                color: #717070;
                            }
                            .tagline {
                                text-align: center;
                                color: #FFFFFF;
                                margin-top: 4px;
                                font-weight: lighter;
                                text-transform: uppercase;
                                letter-spacing: 1px;
                            }

                            .banner {
                                background-color: #2D9AB7;
                                background-image: url(../images/parallax.png);
                                +height:"""+str(tamaño)+"""px;
                                background-attachment: fixed;
                                background-size: cover;
                                background-repeat: no-repeat;
                            }
                            .parallaxx {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 50px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }
                            .parallax {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }

                            .paralla {
                                color: #ffffff5e;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }


                            .copyright {
                                text-align: center;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: #717070;
                                color: #ffffff;
                                text-transform: uppercase;
                                font-weight: lighter;
                                letter-spacing: 2px;
                                border-top-width: 2px;
                            }
                            """
    g = open("CSS\pa.css",'wb')
    g.write(bytes(css,"ascii"))
    g.close()
    f = open('Lexemas.html','wb')
    f.write(bytes(mensaje,"ascii"))
    f.close()
    webbrowser.open_new_tab('Lexemas.html')

def cargaOrden():
    global archivoOrden
    global archivo_Orden_Seleccionado
    global name
    root = Tk()
    factura.clear()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    archivoOrden = askopenfilename(initialdir="D:\Galeria\Escritorio\Material U\LFP\Tareas\LFP_Proyecto1_201709015",filetypes =(("Archivo LFP", "*.lfp"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()
    print("Archivo Orden seleccionada correctamente")
    archivo_Orden_Seleccionado = True
    at = automata(archivoOrden)

def numerico(valorInicial):
    valor = ''
    x = 0
    actual = ''
    state  =  10
    decimal = 2
    while x<len(valorInicial):
        actual = valorInicial[x]
        if state == 10: #veficia que no haya datos desconocidos en numeros
            if ord(actual) >= 48 and ord(actual) <= 57:
                valor = valor + actual
                x=x+1
            elif ord(actual) == 46:
                valor = valor + actual
                x=x+1
                state = 11
    ####################################################################33
        elif state == 11: #verifica que des pues del punto hayan unicamente 2 ceros
            if decimal == 2 and ord(actual) >= 48 and ord(actual) <= 57:
                valor = valor + actual
                decimal = decimal - 1 
                x=x+1
            elif decimal == 1 and ord(actual) >= 48 and ord(actual) <= 57:
                x = x + 1
                aux = valorInicial[x]
                if ord(aux) >=48 and ord(aux) <= 57:
                    if int(aux) > 4:
                        f = int(actual)+1
                        valor = valor + str(f)
                    else:
                        valor = valor + actual
                else:
                    valor = valor + actual
                decimal = decimal - 1
                x=x+1
    if  decimal == 1:
        valor = valor + '0'
        x=x+1
    elif decimal == 2:
        valor = valor + '00'
        x = x + 1
    return valor

def generarMenu():
    if archivo_Menu_Seleccionado == False:
        print("Seleccione archivo de Menu previamente")
    else:
        if errores == []:

            mensaje= """<!doctype html>
                        <html>
                        <head>
                        <title>MENU</title>
                        <link href="CSS\pariencia.css" rel="stylesheet" type="text/css">
                        </head>
                        <body>
                        <div class="container"> 
                        <header> <a href="">
                        <h6 class="logo">MENU</h6>
                        </a>
                        <nav>
                        <ul>
                        </ul>
                        </nav>
                        </header>
                        <section class="hero" id="hero">
                        <h3 class="hero_header">RESTAURANTE  <span class="light">"""
            mensaje = mensaje + name
            me = """</span></h3>
                        <p class="tagline">Menu</p>
                        </section>
                        <section class="banner">"""
            mensaje = mensaje + me
            tamaño = 75
            for lista in matrizArticulos:
                mensaje = mensaje + """<h1 class="parallaxx">"""+lista[0]+""" </h1>"""
                tamaño = tamaño + 125
                for i in range(1,len(lista)):
                    tamaño = tamaño + 110
                    mensaje = mensaje + """<h3 class="parallax">"""+lista[i]['nombre']+" Q."+lista[i]['precio']+"""</h3>"""
                    mensaje = mensaje + """<h5 class="paralla">"""+lista[i]['descripcion']+"""</h5>"""

            for i in range(4):
                mensaje = mensaje + """<h1 class="paralla"> </h1>"""
            mi = """<div class="copyright">&copy;2020- <strong>Edwin estuardo reyes reyes</strong></div>
                        </div>
                        </body>
                        </html>"""
            mensaje = mensaje + mi

            css = """@charset "UTF-8";
                    /* Body */
                    html {
                            font-size: 40px;
                        }
                        body {
                            font-family: source-sans-pro;
                            background-color: #f2f2f2;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            font-style: normal;
                            font-weight: 200;
                            }
                            .container {
                            width: 70%;
                            margin-left: auto;
                            margin-right: auto;
                            height: 700px;
                                        }
                            header {
                            width: 100%;
                            height: 8%;
                            background-color: #52bad5;
                            border-bottom: 1px solid #2C9AB7;
                            }
                            .logo {
                        color: #fff;
                            font-weight: bold;
                            text-align: undefined;
                            width: 10%;
                            float: left;
                            margin-top: 15px;
                            margin-left: 25px;
                            letter-spacing: 4px;
                                }
                            .hero_header {
                            color: #FFFFFF;
                            text-align: center;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            letter-spacing: 4px;
                                }
                            .hero {
                            background-color: #B3B3B3;
                            padding-top: 100px;
                            padding-bottom: 80px;
                            }
                            .light {
                                font-weight: bold;
                                color: #717070;
                            }
                            .tagline {
                                text-align: center;
                                color: #FFFFFF;
                                margin-top: 4px;
                                font-weight: lighter;
                                text-transform: uppercase;
                                letter-spacing: 1px;
                            }

                            .banner {
                                background-color: #2D9AB7;
                                background-image: url(../images/parallax.png);
                                +height:"""+str(tamaño)+"""px;
                                background-attachment: fixed;
                                background-size: cover;
                                background-repeat: no-repeat;
                            }
                            .parallaxx {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 50px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }
                            .parallax {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }

                            .paralla {
                                color: #ffffff5e;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }


                            .copyright {
                                text-align: center;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: #717070;
                                color: #ffffff;
                                text-transform: uppercase;
                                font-weight: lighter;
                                letter-spacing: 2px;
                                border-top-width: 2px;
                            }
                            """
            g = open("CSS\pariencia.css",'wb')
            g.write(bytes(css,"ascii"))
            g.close()
            f = open('Menu.html','wb')
            f.write(bytes(mensaje,"ascii"))
            f.close()
            webbrowser.open_new_tab('Menu.html')
        else:
            mensaje =  """<!doctype html>
                        <html>
                        <head>
                        <title>ERRORES</title>
                        <link href="CSS\par.css" rel="stylesheet" type="text/css">
                        </head>
                        <body>
                        <div class="container"> 
                        <header> <a href="">
                        <h6 class="logo">REPORTE</h6>
                        </a>
                        </header>
                        <section class="hero" id="hero">
                        <h3 class="hero_header">INFORME DE ERRORES</h3>
                        <p class="tagline">Menu</p>
                        </section>
                        <section class="banner">
                        <div style="text-align:center;">
                        <table  border=1 bordercolor="white"  style="margin: 0 auto;bgcolor="#FFFFFF">
                        <tr>
                         <td><font color = "white">id</td><td><font color = "white">Fila</td><td><font color = "white">Columna</td><td><font color = "white">Caracter</td><td><font color = "white">Descripcion</td>
                        </tr>"""
            i = 1
            tamaño = 20
            for error in errores:    
                mensaje = mensaje + """<tr><td><font color = "white">"""+str(i)+"""</td><td><font color = "white">"""+str(error['Fila'])+"""</td><td><font color = "white">"""+str(error['Columna'])+"""</td><td><font color = "white">"""+error['Caracter']+"""</td><td><font color = "white">"""+error['Descripcion']+"""</td></tr>"""
                i = i + 1
                tamaño = tamaño + 38
            mens =""" </table> </div> <div class="copyright">&copy;2020- <strong>Edwin estuardo reyes reyes</strong></div>
                        </div>
                        </body>
                        </html>"""
            mensaje = mensaje + mens
            css = """@charset "UTF-8";
                    /* Body */
                    html {
                            font-size: 30px;
                        }
                        body {
                            font-family: source-sans-pro;
                            background-color: #f2f2f2;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            font-style: normal;
                            font-weight: 200;
                            }
                            .container {
                            width: 70%;
                            margin-left: auto;
                            margin-right: auto;
                            height: 700px;
                                        }
                            header {
                            width: 100%;
                            height: 8%;
                            background-color: #52bad5;
                            border-bottom: 1px solid #2C9AB7;
                            }
                            .logo {
                        color: #fff;
                            font-weight: bold;
                            text-align: undefined;
                            width: 10%;
                            float: left;
                            margin-top: 15px;
                            margin-left: 25px;
                            letter-spacing: 4px;
                                }
                            .hero_header {
                            color: #FFFFFF;
                            text-align: center;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            letter-spacing: 4px;
                                }
                            .hero {
                            background-color: #B3B3B3;
                            padding-top: 100px;
                            padding-bottom: 80px;
                            }
                            .light {
                                font-weight: bold;
                                color: #717070;
                            }
                            .tagline {
                                text-align: center;
                                color: #FFFFFF;
                                margin-top: 4px;
                                font-weight: lighter;
                                text-transform: uppercase;
                                letter-spacing: 1px;
                            }

                            .banner {
                                background-color: #2D9AB7;
                                background-image: url(../images/parallax.png);
                                +height:"""+str(tamaño)+"""px;
                                background-attachment: fixed;
                                background-size: cover;
                                background-repeat: no-repeat;
                            }
                            .parallaxx {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 50px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }
                            .parallax {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }

                            .paralla {
                                color: #ffffff5e;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }


                            .copyright {
                                text-align: center;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: #717070;
                                color: #ffffff;
                                text-transform: uppercase;
                                font-weight: lighter;
                                letter-spacing: 2px;
                                border-top-width: 2px;
                            }
                            """
            g = open("CSS\par.css",'wb')
            g.write(bytes(css,"ascii"))
            g.close()
            f = open('Errores.html','wb')
            f.write(bytes(mensaje,"ascii"))
            f.close()
            webbrowser.open_new_tab('Errores.html')

def generarFactura():
    total = 0.00
    if archivo_Menu_Seleccionado == False:
        print("Porfavor cargue al sistemas el archivo Menu")
    elif archivo_Orden_Seleccionado == False:
        print("Porfavor cargue al sistemas el archivo Orden")
    else:
        if errores == []:
            mensaje= """<!doctype html>
                        <html>
                        <head>
                        <title>ERRORES</title>
                        <link href="CSS\ctura.css" rel="stylesheet" type="text/css">
                        </head>
                        <body>
                        <div class="container">        
                        </header>
                        <section class="banner">"""
            tamaño = 450
            mensaje = mensaje + """<h1 class="titulo">Restaurante """+nombreRestaurante+""" </h1>"""
            mensaje = mensaje + """<h1 class="titulo1"> Factura No. 01 </h1>"""
            mensaje = mensaje + """<h1 class="titulo1">Fecha: """+datetime.now().strftime('%d/%m/%Y')+"""</h1>"""
            mensaje = mensaje + """<h1 class="titulo1"></h1>"""
            mensaje = mensaje + """<h1 class="titulo1"></h1>"""
            mensaje = mensaje + """<h1 class="titulo1"></h1>"""
            mensaje = mensaje + """<h1 class="titulo2">Datos del Cliente:</h1>"""
            mensaje = mensaje + """<h1 class="titulo2">Nombre: """+factura[0]['nombre']+""" </h1>"""
            mensaje = mensaje + """<h1 class="titulo2">Nit: """+factura[0]['nit']+""" </h1>"""
            mensaje = mensaje + """<h1 class="titulo2">Direccion: """+factura[0]['direccion']+""" </h1>"""
            mensaje = mensaje + """<div style="text-align:center;">
                        <table style="margin: 0 auto;bgcolor="#FFFFFF">
                        <tr>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b><font color = "white">|-</font>Cantidad<font color = "white">- </font></b> </td>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b> <font color = "white">|-------------</font>Concepto<font color = "white">-------------</font></b> </td>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b> <font color = "white">|-</font>Precio<font color = "white">-</font>     </b> </td>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b> <font color = "white">|-</font>Total<font color = "white">-| </font>   </b> </td>   
                        </tr>"""
            for i in range(1, len(factura)):
                for categoria in matrizArticulos:
                    for item in range(1,len(categoria)):
                        if categoria[item]['ID'] == factura[i]['id']:
                            tamaño = tamaño + 36
                            final = numerico(str(float(categoria[item]['precio'])*float(factura[i]['numero'])))
                            total = total + float(final)
                            mensaje = mensaje +  """ <tr>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b>"""+factura[i]['numero']+"""</b> </td>
                        <td  style="color:#2c9ab7;text-align:left;font-size:150%;font-family: source-sans-pro;" ><b> """+categoria[item]['descripcion']+"""</b> </td>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b> Q."""+categoria[item]['precio'] +"""</b> </td>
                        <td  style="color:#2c9ab7;font-size:150%;font-family: source-sans-pro;" ><b> Q."""+str(final) +"""</b> </td>
                        </tr>"""
            tamaño = tamaño + 260
            mensaje = mensaje + """</table> </div><h1 class="titulo1">------------------------------------------------------------</h1>"""
            ntotal = numerico(str(total))
            mensaje = mensaje + """<h1 class="titulo1">Sub total<font color = "white">------------------------------------------</font>Q."""+ntotal+"""</h1>"""
            des = str(float(factura[0]['descuento'])*float(total)/100)
            descuento = numerico(des)
            mensaje = mensaje + """<h1 class="titulo1">Propina("""+str(factura[0]['descuento'])+"""%)<font color = "white">------------------------------------</font> Q."""+descuento+""" </h1>""" 
            mensaje = mensaje + """<h1 class="titulo1">------------------------------------------------------------</h1>"""
            t = float(ntotal)+float(descuento)
            mensaje = mensaje + """<h1 class="titulo1">Total<font color = "white">-----------------------------------------------</font>Q."""+str(t)+"""</h1>""" 
            mensaje = mensaje + """<h1 class="titulo1"> </h1>"""
            mi = """<div class="copyright">&copy;2020- <strong>Edwin estuardo reyes reyes</strong></div>
                        </div>
                        </body>
                        </html>"""
            mensaje = mensaje + mi

            css = """@charset "UTF-8";
                    /* Body */
                    html {
                            font-size: 20px;
                        }
                        body {
                            font-family: source-sans-pro;
                            background-color: #b8b8b8;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            font-style: normal;
                            font-weight: 200;
                            }
                            .container {
                            width: 55%;
                            margin-left: auto;
                            margin-right: auto;
                            height: 700px;
                                        }
                            header {
                            width: 100%;
                            height: 8%;
                            background-color: #52bad5;
                            border-bottom: 1px solid #2c9ab7;
                            }
                            .logo {
                        color: #fff;
                            font-weight: bold;
                            text-align: undefined;
                            width: 10%;
                            float: left;
                            margin-top: 15px;
                            margin-left: 25px;
                            letter-spacing: 4px;
                                }
                            .hero_header {
                            color: #FFFFFF;
                            text-align: center;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            letter-spacing: 4px;
                                }
                            .hero {
                            background-color: #B3B3B3;
                            padding-top: 100px;
                            padding-bottom: 80px;
                            }
                            .light {
                                font-weight: bold;
                                color: #717070;
                            }
                            .tagline {
                                text-align: center;
                                color: #FFFFFF;
                                margin-top: 4px;
                                font-weight: lighter;
                                text-transform: uppercase;
                                letter-spacing: 1px;
                            }

                            .banner {
                                background-color: #FFFFFF;
                                background-image: url(../images/parallax.png);
                                height:"""+str(tamaño)+"""px;
                                background-attachment: fixed;
                                background-size: cover;
                                background-repeat: no-repeat;
                            }
                        
                            .titulo {
                                color: #2c9ab7;
                                text-align:center;
                            
                                padding-top: 50px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }

                            .titulo1{
                                color: #2c9ab7;
                                text-align: center;   
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }
                            .titulo2{
                                color: #2c9ab7;
                                text-align: left;
                                padding-left: 30px;   
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }


                            .copyright {
                                text-align: center;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: #717070;
                                color: #ffffff;
                                text-transform: uppercase;
                                font-weight: lighter;
                                letter-spacing: 2px;
                                border-top-width: 2px;
                            }
                            """
            g = open("CSS\ctura.css",'wb')
            g.write(bytes(css,"ascii"))
            g.close()
            f = open('factura.html','wb')
            f.write(bytes(mensaje,"ascii"))
            f.close()
            webbrowser.open_new_tab('factura.html')

        
        else:
            mensaje =  """<!doctype html>
                        <html>
                        <head>
                        <title>ERRORES</title>
                        <link href="CSS\par.css" rel="stylesheet" type="text/css">
                        </head>
                        <body>
                        <div class="container"> 
                        <header> <a href="">
                        <h6 class="logo">REPORTE</h6>
                        </a>
                        </header>
                        <section class="hero" id="hero">
                        <h3 class="hero_header">INFORME DE ERRORES</h3>
                        <p class="tagline">Menu</p>
                        </section>
                        <section class="banner">
                        <div style="text-align:center;">
                        <table  border=1 bordercolor="white"  style="margin: 0 auto;bgcolor="#FFFFFF">
                        <tr>
                         <td><font color = "white">id</td><td><font color = "white">Fila</td><td><font color = "white">Columna</td><td><font color = "white">Caracter</td><td><font color = "white">Descripcion</td>
                        </tr>"""
            i = 1
            tamaño = 20
            for error in errores:    
                mensaje = mensaje + """<tr><td><font color = "white">"""+str(i)+"""</td><td><font color = "white">"""+str(error['Fila'])+"""</td><td><font color = "white">"""+str(error['Columna'])+"""</td><td><font color = "white">"""+error['Caracter']+"""</td><td><font color = "white">"""+error['Descripcion']+"""</td></tr>"""
                i = i + 1
                tamaño = tamaño + 38
            mens =""" </table> </div> <div class="copyright">&copy;2020- <strong>Edwin estuardo reyes reyes</strong></div>
                        </div>
                        </body>
                        </html>"""
            mensaje = mensaje + mens
            css = """@charset "UTF-8";
                    /* Body */
                    html {
                            font-size: 30px;
                        }
                        body {
                            font-family: source-sans-pro;
                            background-color: #f2f2f2;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            font-style: normal;
                            font-weight: 200;
                            }
                            .container {
                            width: 70%;
                            margin-left: auto;
                            margin-right: auto;
                            height: 700px;
                                        }
                            header {
                            width: 100%;
                            height: 8%;
                            background-color: #52bad5;
                            border-bottom: 1px solid #2C9AB7;
                            }
                            .logo {
                        color: #fff;
                            font-weight: bold;
                            text-align: undefined;
                            width: 10%;
                            float: left;
                            margin-top: 15px;
                            margin-left: 25px;
                            letter-spacing: 4px;
                                }
                            .hero_header {
                            color: #FFFFFF;
                            text-align: center;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            letter-spacing: 4px;
                                }
                            .hero {
                            background-color: #B3B3B3;
                            padding-top: 100px;
                            padding-bottom: 80px;
                            }
                            .light {
                                font-weight: bold;
                                color: #717070;
                            }
                            .tagline {
                                text-align: center;
                                color: #FFFFFF;
                                margin-top: 4px;
                                font-weight: lighter;
                                text-transform: uppercase;
                                letter-spacing: 1px;
                            }

                            .banner {
                                background-color: #2D9AB7;
                                background-image: url(../images/parallax.png);
                                +height:"""+str(tamaño)+"""px;
                                background-attachment: fixed;
                                background-size: cover;
                                background-repeat: no-repeat;
                            }
                            .parallaxx {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 50px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }
                            .parallax {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }

                            .paralla {
                                color: #ffffff5e;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }


                            .copyright {
                                text-align: center;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: #717070;
                                color: #ffffff;
                                text-transform: uppercase;
                                font-weight: lighter;
                                letter-spacing: 2px;
                                border-top-width: 2px;
                            }
                            """
            g = open("CSS\par.css",'wb')
            g.write(bytes(css,"ascii"))
            g.close()
            f = open('Errores.html','wb')
            f.write(bytes(mensaje,"ascii"))
            f.close()
            webbrowser.open_new_tab('Errores.html')

def graphi():
    if archivo_Menu_Seleccionado == False:
        print("Archivo de datos de entrada no seleccionado previamente")
    else:
        g = Digraph('unix', filename='Menu',node_attr={'color': 'lightblue2', 'style': 'filled'})
        g.edge(name,'Menu')
        for lis in matrizArticulos:
            g.edge('Menu',lis[0])
            text = lis[1]['nombre']+' Q.'+str(lis[1]['precio'])+'\\n'+lis[1]['descripcion']
            g.edge(lis[0],str(text))
            for j in range(2,len(lis)):
                t1 = lis[j-1]['nombre']+' Q.'+str(lis[j-1]['precio'])+'\\n'+lis[j-1]['descripcion']
                t2 = lis[j]['nombre']+' Q.'+str(lis[j]['precio'])+ '\\n' +lis[j]['descripcion']
                g.edge(str(t1),str(t2)) #UNO DETRAS DE OTRO
                #g.edge(lis[0],t2)  #TODOS APUNTAN A CATEGORIA
        g.view()
    

while salida == False:
    cls()
    print("          Proyecto 1 - LFP")
    print("")
    print(" Edwin Estuardo Reyes Reyes 201709015")
    print("")
    print("          1. Cargar Menu")
    print("          2. Cargar Orden")
    print("          3. Generar Menu")
    print("          4. Generar Factura")
    print("          5. Generar Arbol")
    print("          6. Salida")
    print("")
    a = input("      Seleccione una opcion: ")
    if (a == '1'):
        cargaMenu()
        a = input()
    elif (a == '2'):
        cargaOrden()
        a = input()
    elif (a == '3'):
        generarMenu()
        a = input()
    elif (a == '4'):
        generarFactura()
        a = input()
    elif (a == '5'):
        graphi()
        a = input()
    elif (a == '6'):
        a=input()
        salida = True
    else:
        print("Opcion "+a+" no se encuentra entre las opciones")