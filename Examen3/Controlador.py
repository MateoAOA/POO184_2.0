from tkinter import messagebox
import sqlite3
import bcrypt

class controlador:
    def __init__(self):
        pass
    
    
    def conexionBD(self):
        
        try:
            conexion=sqlite3.connect("C:/Users/mateo/Documents/POO184/Examen3/Ferreteria.db")
            
            print("Conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se puede conectar")
            
            
            
            
    def guardarMaterial(self,mat,cad):
        
        conx= self.conexionBD()
        
        if(mat == "" or cad==""):
            messagebox.showwarning("El registro no es correcto, pruebe otra vez")
            conx.close()
        else:
            #preparar datos de sql
            cursor= conx.cursor()
            datos=(mat,cad)
            qrInser="insert into MatConstruccion(Material,Cantidad) values(?,?)"
            
            #proceder a insertar y cerramos la conexion
            cursor.execute(qrInser, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito"," Se guardo el Material")        
    
    
    
    
    def consultarTodo(self):
        conx= self.conexionBD()
        
        try:
            cursor= conx.cursor()
            sqlSelect="select * From MatConstruccion"
            
            cursor.execute(sqlSelect)
            consult= cursor.fetchall()
            conx.close()
            
            return consult
        
        except sqlite3.OperationalError:
                print("Error Consulta")    
    
    
    