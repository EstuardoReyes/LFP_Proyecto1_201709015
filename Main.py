from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


archivoMenu = ''
archivoOrden = ''
salida = False
archivo_Menu_Seleccionado = False
archivo_Orden_Seleccionado = False

def cls():
    r=0
    while r<10:
        print("")
        r=r+1 

def cargaMenu():
    global archivoMenu
    global archivo_Menu_Seleccionado
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    archivoMenu = askopenfilename(initialdir="D:\Galeria\Escritorio",filetypes =(("Archivo LFP", "*.lfp"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()
    print("Archivo Menu seleccionada correctamente")
    archivo_Menu_Seleccionado = True

def cargaOrden():
    global archivoOrden
    global archivo_Orden_Seleccionado
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    archivoOrden = askopenfilename(initialdir="D:\Galeria\Escritorio",filetypes =(("Archivo LFP", "*.lfp"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()
    print("Archivo Orden seleccionada correctamente")
    archivo_Orden_Seleccionado = True


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
        #escribir()
        a = input()
    elif (a == '4'):
        #estudiante()
        a = input()
    elif (a == '5'):
        #graphi()
        a = input()
    elif (a == '6'):
        a=input()
        salida = True
    else:
        print("Opcion "+a+" no se encuentra entre las opciones")