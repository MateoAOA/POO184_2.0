from tkinter import Tk, Button, Frame, messagebox

def Mostrar_Mensajes():
    messagebox.showinfo("Aviso:","Presionaste el boton azul")


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

botonVerde= Button(seccion3, text="Boton Verde", fg="black", bg="green")
botonVerde.config(height=2, width=10)
botonVerde.pack()

#llamamos al main
ventana.mainloop()

