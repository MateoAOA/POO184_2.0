from tkinter import Tk, Button, Frame, messagebox, Label, Entry
from Usuario import *
import random
#solicitar datos

ventana= Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("1000x600")

titulo= Label(ventana,text="LOGIN", font=("Berlin Sans FB Demi",20),bg="#660FC3")
titulo.pack()

iNombre= Label(ventana,text="Escribe tu nombre", font=("Berlin Sans FB Demi",20),bg="#660FC3")
iNombre.pack()
Nombre= Entry(ventana, text="Nombre: ", font=("Berlin Sans FB Demi",20), bg="#A170D6")
Nombre.pack()

iApellido_Paterno= Label(ventana,text="Escribe tu Apellido paterno", font=("Berlin Sans FB Demi",20),bg="#660FC3")
iApellido_Paterno.pack()
Apellido_Paterno= Entry(ventana, font=("Berlin Sans FB Demi",20), bg="#A170D6")
Apellido_Paterno.pack()

iApellido_Materno= Label(ventana,text="Escribe tu Apellido materno", font=("Berlin Sans FB Demi",20),bg="#660FC3")
iApellido_Materno.pack()
Apellido_Materno= Entry(ventana, font=("Berlin Sans FB Demi",20), bg="#A170D6")
Apellido_Materno.pack()

iFecha_Nacimento= Label(ventana,text="Escribe tu fecha de nacimiento:", font=("Berlin Sans FB Demi",20),bg="#660FC3")
iFecha_Nacimento.pack()
Fecha_Nacimento= Entry(ventana, font=("Berlin Sans FB Demi",20), bg="#A170D6")
Fecha_Nacimento.pack()

iCarrera= Label(ventana,text="Escribe tu carrera:", font=("Berlin Sans FB Demi",20),bg="#660FC3")
iCarrera.pack()
Carrera= Entry(ventana, font=("Berlin Sans FB Demi",20), bg="#A170D6")
Carrera.pack()

#crear objeto de la clase personaje
matricula = Usuario(random(Nombre, Apellido_Paterno, Apellido_Materno, Fecha_Nacimento, Carrera))

#usar atrivutos y metods
matricula.setNombre("Matricula Escolar")


print("")
print("####### Matricula Generada #")
matricula.generar()




#llamamos al main
ventana.mainloop()