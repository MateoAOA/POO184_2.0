from tkinter import*
from tkinter import ttk
import tkinter as tk
from controladorBD import*
from tkinter import messagebox
from tkinter.messagebox import showinfo

#crear un objeto tipo controlador
controlador= controladorBD()

#proceder a guadar el metodo guardarUsuario() del objeto controlador
def ejecutarInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

def ejecutaSelectU():
    rsUsuario=controlador.consultarUsuario(varbus.get())
    for usu in rsUsuario:
        cadena=str(usu[0])+" "+ usu[1]+ " "+ usu[2]+ " "+ str(usu[3])
        
    if(rsUsuario):
        print(cadena)
    else:
        messagebox.showinfo("Usuario no registrado en la base de datos")

def ejecutaConsultarU():
    usuarios= controlador.consultarTodos()
    tree.delete(*tree.get_children())
    for i in usuarios:
        tree.insert("", "end", text=i[0], values=(i[1], i[2], i[3]))

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
titulo= Label(pestana1, text="Resgistro de Usurios", fg="blue", font=("Modern",18) ).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1, text="nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom ).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text="correo: ").pack()
txtcor= Entry(pestana1, textvariable=varCor ).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text="contraseña: ").pack()
txtcon= Entry(pestana1, textvariable=varCon ).pack()

btnGuardar= Button(pestana1, text="Guardar Usuario", command=ejecutarInsert).pack()

#pestaña 2 Buscar Usuario
titulo2= Label(pestana2, text="Buscar Usurios", fg="green", font=("Modern",18) ).pack()

varbus= tk.StringVar()
lblid= Label(pestana2, text="Identificador de usuario: ").pack()
txtid= Entry(pestana2, textvariable=varbus ).pack()
btnBusqueda= Button(pestana2, text="Buscar",command=ejecutaSelectU).pack()

subBus= Label(pestana2,text="Registrado: ",fg="blue",font=("Modern",15)).pack()
texBus=tk.Text(pestana2,height=5,width=52).pack()


#pestaña 3 consulta usuarios
titulo3= Label(pestana3, text="Consultar Usurios", fg="green", font=("Modern",18) ).pack()

encabezado=(1,2,3,4)

tree = ttk.Treeview(pestana3,columns=encabezado,show="headings")
tree.heading(1,text="ID")
tree.heading(2,text="Nombre")
tree.heading(3,text="Correo")
tree.heading(4,text="contraseña")
tree.pack()

btnConsultar= Button(pestana3, text="Consultar",command=ejecutaConsultarU).pack()





panel.add(pestana1, text="Formulario de Usuarios")
panel.add(pestana2, text="Buscar Usuarios")
panel.add(pestana3, text="Consultar Usuario")
panel.add(pestana4, text="Actualiar Usuario")





ventana.mainloop()


