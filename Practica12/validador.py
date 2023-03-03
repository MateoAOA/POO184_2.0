from tkinter import messagebox

#metodo
def Mensaje (correo,password):
    print(correo,password)
    if(correo=="12345@gmail.com" and password=="12345"):
        messagebox.showinfo("Aviso:","Bienvenido")
    else:
        messagebox.showerror("Error:","DATOS INCORRECTOS")

        