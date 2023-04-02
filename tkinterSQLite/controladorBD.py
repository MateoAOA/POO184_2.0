from tkinter import messagebox
import sqlite3
import bcrypt




#preparamos conexion
class controladorBD:
    
    def __init__(self):
        pass
    
    
    def conexionBD(self):
        
        try:
            conexion=sqlite3.connect("C:/Users/mateo/Documents/POO184/tkinterSQLite/DataBases.db")
            print("Conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se puede conectar")
    
       
    def guardarUsuario(self,nom,cor,con):
        
        #llamar a la conexion
        conx= self.conexionBD()
        
        #revisar parametros vacios
        if(nom == "" or cor=="" or con == ""):
            messagebox.showwarning("aguas!, Revisa tu formulario")
            conx.close()
        else:
            #preparar datos de sql
            cursor= conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInser="insert into Usuarios(nombre,correo,contra) values(?,?,?)"
            
            #proceder a insertar y cerramos la conexion
            cursor.execute(qrInser, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito"," Se guardo el Usuario")
            
    def encriptarCon(self,con):
        conplana= con
        conplana= conplana.encode()
        sal= bcrypt.gensalt()
        conHa=bcrypt.hashpw(conplana,sal)
        print(conHa)
        
        return conHa
        
        
    def consultarUsuario(self,id):
        #1.preparar conexion
        conx=self.conexionBD()
            
        #2.verificar que el ID no este vacio
        if( id == ""):
            messagebox.showwarning("cuidado","ID vacio escribe uno valido")
        else:
            #proceder a buscar
            try:
            #preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * From Usuarios where id=" + id
                
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error Consulta")
                
                
    def consultarTodos(self):
        conx= self.conexionBD()
        
        try:
            cursor= conx.cursor()
            sqlSelect="select * From Usuarios"
            
            cursor.execute(sqlSelect)
            consult= cursor.fetchall()
            conx.close()
            
            return consult
        
        except sqlite3.OperationalError:
                print("Error Consulta")
    
   
    
    