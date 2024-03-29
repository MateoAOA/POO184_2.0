from tkinter import Tk, Button, Frame, messagebox, Label, Entry

#metodo
def Mensaje ():
    if(correo.get()=="12345@gmail.com" and password.get()=="12345"):
        messagebox.showinfo("Aviso:","Bienvenido")
    else:
        messagebox.showerror("Error:","DATOS INCORRECTOS")

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
titulo= Label(seccion1,text="LOGIN", font=("Berlin Sans FB Demi",50),bg="#660FC3")
titulo.place(x=400, y=100)

#Correo
usuario= Label(seccion2, text="Correo Electronico:", font=("Berlin Sans FB Demi",20), bg="#A170D6") 
usuario.pack()

correo= Entry(seccion2, font=("Berlin Sans FB Demi",15),width=25)
correo.pack()



#CONTRASEÑA
contraseña= Label(seccion2, text="Contraseña:", font=("Berlin Sans FB Demi",20), bg="#A170D6") 
contraseña.pack()

password= Entry(seccion2, font=("Berlin Sans FB Demi",15),width=25)
password.config(show="*")
password.pack()


# boton ingresar
boton= Button(seccion2, text="Ingresar", fg="black", command= Mensaje)
boton.place(x=480, y=140)

#llamamos al main (sin esto no imprime la ventana)
ventana.mainloop()





# Función para generar un número aleatorio
def generar_numero():
    numero = random.randint(1, 100)
    label_numero.config(text="Número generado: " + str(numero))

# Crear un botón que genere un número aleatorio
boton_generar = tk.Button(root, text="Generar número", command=generar_numero)
boton_generar.pack()

# Crear una etiqueta para mostrar el número generado
label_numero = tk.Label(root, text="")
label_numero.pack()

# Ejecutar la aplicación
root.mainloop()
En este ejemplo, utilizamos la función randint del módulo random para generar un número entero aleatorio entre 1 y 100 cada vez que se hace clic en el botón "Generar número". Luego, actualizamos la etiqueta label_numero para mostrar el número generado.





