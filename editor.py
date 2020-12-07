# importamos tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from io import open

# VARIABLE GLOBAL - la utilizaremeso para almacenar la ruta de un fichero
ruta =''

# FUNCIONES
def nuevo():
    global ruta # para indicarle que ruta es una variable global
    mensaje.set('nuevo fichero')
    texto.delete(1.0,'end') # que borre desde el carecter n1 al final del todo
    root.title(ruta + '- Mi editor')



def abrir():
    global ruta
    mensaje.set('abrir fichero')
    ruta = filedialog.askopenfilename(
        initialdir='',
        filetype=(('fichero de texto','*.txt'),),
        title='abrir un fichero')

    if ruta is not '':
        fichero = open(ruta,'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + '- Mi editor')

def guardar():
    global ruta
    mensaje.set('guardar fichero')
    if ruta is not '':
        # el ultimo caracter es un salto de linea , por eso ponemos end-1c
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        messagebox.showinfo('Guardado', 'Fichero guardado correctamente')
        mensaje.set('fichero guardado correctamente')       
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set(' guardar fichero como')  
    fichero = filedialog.asksaveasfile(title='Guardar fichero', mode='w', defaultextension='.txt')
    if fichero is not None:
        ruta = fichero.name 
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        messagebox.showinfo('Guardado', 'Fichero guardado correctamente')
        mensaje.set('fichero guardado correctamente')
    else:
        mensaje.set('guardado cancelado')
        ruta = ''

#ELEGIR UN COLOR
def color_texto():
    color= colorchooser.askcolor(title='que color quieres')
    color_text= color[1]
    texto.config(fg='{}'.format(color_text))
    color_editor.config(fg='{}'.format(color_text))
def color_fondo():
    color= colorchooser.askcolor(title='que color quieres')
    color_bg= color[1]
    texto.config(bg='{}'.format(color_bg))
    
# FUENTES
def arial():
    fuente.set('Arial')
    texto.config(font=('Arial',12))
def calibri():
    fuente.set('Calibri')
    texto.config(font=('Calibri',12))
def lucida():
    fuente.set('Lucida Console')
    texto.config(font=('Lucida Console',12))
def comic():
    fuente.set('Comic Sans MS')
    texto.config(font=('Comic Sans MS',12))


# CREAR LA RAIZ

root = Tk()
# TITULO DE LA VENTANA
root.title('Editor Personal')
root.iconbitmap('almacen.ico')

# Menu superior

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Nuevo',command=nuevo)
filemenu.add_command(label='Abrir',command=abrir)
filemenu.add_command(label='Guardar',command=guardar)
filemenu.add_command(label='Guardar Como',command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)

formatmenu = Menu(menubar,tearoff=0)
formatmenu.add_command(label='Color Texto', command=color_texto)
formatmenu.add_command(label ='Color Fondo',command=color_fondo)

fuentemenu = Menu(menubar,tearoff=0)
fuentemenu.add_command(label='Arial',command=arial)
fuentemenu.add_command(label='Calibri',command=calibri)
fuentemenu.add_command(label='Lucida Console',command = lucida)
fuentemenu.add_command(label='Comic Sans MS',command= comic)

menubar.add_cascade(menu=filemenu, label='Archivo')
menubar.add_cascade(menu=formatmenu, label='Color')
menubar.add_cascade(menu=fuentemenu,label='Fuente')


root.config(menu=menubar)

# caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(bd=0,padx=6, pady=4, font=('Comic-sand',12))

# monitor inferior
mensaje= StringVar()
fuente= StringVar()
mensaje.set('Bienvenido')
monitor =Label(root,textvar=mensaje, justify='left')
monitor.pack(side='left')
color_editor = Label(root,text='Color Texto', justify= 'center')
color_editor.pack(side='right',padx=20)
fuente.set('Arial')
tipo_fuente=Label(root,textvar=fuente, justify='right')
tipo_fuente.pack(side='right')


# SIEMPRE TIENE QUE IR ABAJO . 
root.mainloop()