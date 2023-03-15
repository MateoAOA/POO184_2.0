from tkinter import Tk, Button, Frame, messagebox, Label, Entry
from Usuario import *
#solicitar datos

ven= Tk()
ven.title("Sistma UPQ")
ven.geometry("600x400")


titulo= Label(ven,text="Generador de Matriculas", font=("Berlin Sans FB Demi",50),bg="#660FC3")
titulo.pack()

ind_nombre = Label(ven, text="Coloque su nombre:")
ind_nombre.grid(row=4, column=0, sticky="w")

col_nombre = Entry(ven, font=("Berlin Sans FB Demi",15), width=25)
col_nombre.grid(row=5, column=0)

ind_apellidop = Label(ven, text="Coloque su nombre:")
ind_apellidop.grid(row=6, column=1, sticky="w")

col_apellidom = Entry(ven, font=("Berlin Sans FB Demi",15), width=25)
col_apellidom.grid(row=7, column=1)


print("")
print("#Datos #")
Nombre= input("Escibir tu nombre: ")
Apellido_Paterno= input("Escibir tu apellido paterno: ")
Apellido_Materno= input("Escibir tu apellido materno: ")
Fecha_Nacimento= input("Escribe tu fecha de nacimiento: ")
Carrera= input("Escribe tu carrera: ")

#crear objeto de la clase personaje

matricula = Usuario(Nombre, Apellido_Paterno, Apellido_Materno, Fecha_Nacimento, Carrera)

#usar atrivutos y metods

matricula.setNombre("Matricula Escolar")


print("")
print("####### Matricula Generada #")
matricula.generar()

#llamamos al main
ven.mainloop()