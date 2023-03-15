from tkinter import Tk, Button, Frame, messagebox, Label, Entry, Checkbutton
import generador

def __init__ (self,length,include_special,password):
    self.__length, int(value=8)
    self.__include_uppercase, bool(value=True)
    self.__include_special, bool(value=False)
    self.__password, str(value="")
    


#1.- instanciamos el objeto ventana
ventana= Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("1000x600")

#2.- agregamos los frame
seccion1= Frame(ventana, bg="#660FC3")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana, bg="#A170D6")
seccion2.pack(expand=True,fill='both')

#Titulo
titulo= Label(seccion1,text="Generador de Contraseñas", font=("Berlin Sans FB Demi",50),bg="#660FC3")
titulo.place(x=100, y=100)


#intrucciones
longitud = Label(seccion2, text="Coloque la longitud:")
longitud.grid(row=0, column=0, sticky="w")

mayusculas = Label(seccion2, text="¿Desea incluir mayúsculas?:")
mayusculas.grid(row=1, column=0, sticky="w")

simbolos = Label(seccion2, text="Desea incluir caracteres especiales?:")
simbolos.grid(row=2, column=0, sticky="w")

respuesta = Label(seccion2, text="Contraseña generada:")
respuesta.grid(row=4, column=0, sticky="w")

#botones
longitud2 = Entry(seccion2, textvariable=length)
longitud2.grid(row=0, column=1)

mayusculas2 = Checkbutton(seccion2, variable=self.include_uppercase)
mayusculas2.grid(row=1, column=1, sticky="w")

simbolos2 = Checkbutton(seccion2, variable=self.include_special)
simbolos2.grid(row=2, column=1, sticky="w")

respuesta= Button(seccion2, text="Generar contraseña", command=self.generate_password)
respuesta.grid(row=3, column=0, pady=10)

comprobar = Button(seccion2, text="Comprobar fortaleza", command=self.check_strength)
comprobar.grid(row=3, column=1, pady=10)


#salida
Entry(seccion2, textvariable=self.password, state="readonly").grid(row=4, column=1)

#llamamos al main (sin esto no imprime la ventana)
ventana.mainloop()