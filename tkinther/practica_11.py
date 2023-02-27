from tkinter import Tk, Button, Frame

#1.- instanciamos el objeto ventana
ventana= Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2.- agregamos los frame
seccion1= Frame(ventana, bg="white")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana, bg="blue")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana, bg="red")
seccion3.pack(expand=True,fill='both')

#llamamos al main
ventana.mainloop()