from tkinter import*
from tkinter import ttk
import tkinter as tk

ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

panel= ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#pestaña 1
titulo= Label(pestana1, text="Resgistrp de Usurios", fg="blue", font=("Modern",18) ).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1, text="nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom ).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text="correo: ").pack()
txtcor= Entry(pestana1, textvariable=varCor ).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text="contraseña: ").pack()
txtcon= Entry(pestana1, textvariable=varCon ).pack()

btnGuardar= Button(pestana1, text="Guardar Usuario").pack()




panel.add(pestana1, text="Formulario de Usuarios")
panel.add(pestana2, text="Buscar Usuarios")
panel.add(pestana3, text="Consultar Usuario")
panel.add(pestana4, text="Actualiar Usuario")





ventana.mainloop()


