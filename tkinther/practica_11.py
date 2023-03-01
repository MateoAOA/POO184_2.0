from tkinter import Tk, Button, Frame, messagebox


#5.- declarar la funcion para mensajes
def Mostrar_Mensajes():
    messagebox.showinfo("Aviso:","Presionaste el boton azul")
    messagebox.showerror("Error:","Todo fallo con exito")
    print(messagebox.askokcancel("Pregunta","¿Ella jugo con su corazon?"))

#6.- funcion para agregar botones con un boton
def agregarBoton():
    botonVerde.config(text="+", bg="green",fg="white" )
    botonNuevo= Button(seccion3, text="Nuevo")
    botonNuevo.pack()


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

#3.- Agregamos botones
botonAzul= Button(seccion1, text="Boton Azul", fg="blue", command=Mostrar_Mensajes)
botonAzul.place(x=60, y=60)

botonAmarillo= Button(seccion2, text="Boton Amarillo", fg="white", bg="#ffff4d")
botonAmarillo.grid(row= 1, column= 1)

botonNegro= Button(seccion2, text="Boton Negro", fg="white", bg="black")
botonNegro.grid(row=0 , column=0)

botonVerde= Button(seccion3, text="Boton Verde", fg="black", bg="green", command=agregarBoton)
botonVerde.config(height=2, width=10)
botonVerde.pack()

#4.- posicionamiento de elementos

#llamamos al main
ventana.mainloop()

