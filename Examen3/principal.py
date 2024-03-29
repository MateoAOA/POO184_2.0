from tkinter import*
from tkinter import ttk
import tkinter as tk
from Controlador import*
from tkinter import messagebox
from tkinter.messagebox import showinfo

controlar = controlador()

def ejectGuardar():
    controlar.guardarMaterial(varMat.get(),varCad.get())


def Actualizar_todo():
    cons= controlar.
    result = c.fetchone()
    label.config(text=result[0])

def ejectConsultarTodos():
    materiales= controlar.consultarTodo()
    tree.delete(*tree.get_children())
    for i in materiales:
        tree.insert("", "end", text=i[0], values=(i[0], i[1], i[2]))
        
ventana = Tk()
ventana.title("Ventana Principal")
ventana.geometry("700x300")

panel= ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)


#pestaña 1
titulo= Label(pestana1, text="Resgistro de Material", fg="black", font=("Modern",18) ).pack()
varMat= tk.StringVar()
lblNom= Label(pestana1, text="Material: ", fg="black").pack()
txtNom= Entry(pestana1, textvariable=varMat ).pack()

varCad= tk.StringVar()
lblCad= Label(pestana1, text="Cantidad: ",fg="black").pack()
txtcad= Entry(pestana1, textvariable=varCad ).pack()


btnGuardar= Button(pestana1, text="Guardar Material", command=ejectGuardar).pack()



#pestaña 3
titulo3= Label(pestana2, text="Consultar Materiales", fg="black", font=("Modern",18) ).pack()

encabezado=(1,2,3)

tree = ttk.Treeview(pestana2,columns=encabezado,show="headings")
tree.heading(1,text="ID")
tree.heading(2,text="Nombre")
tree.heading(3,text="Cantidad")
tree.pack()

btnConsultar= Button(pestana2, text="Consultar", command=ejectConsultarTodos).pack()
btnActualizar= Button(pestana2, text="Actualizar", command=Actualizar_lista).pack()



#pestañas
panel.add(pestana1, text="Ingresar Material")
panel.add(pestana2, text="Consultar Materiales")



ventana.mainloop()