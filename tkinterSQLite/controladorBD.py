from tkinter import messagebox
import sqlite3
import bcrypt




#preparamos conexion
class controladorBD:
    
    def __init__(self):
        pass
    
    
    def conexionBD(self):
        
        try:
            conexion=sqlite3.connect("https://github.com/MateoAOA/POO184_2.0/blob/eb417b4a5bca0f72e00436192b3e89ddfa3d5ec2/tkinterSQLite/bd.db")
            print("Conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se puede conectar")
    
    
    
    def guardarUsuario(self,nom,cor,con):
        
        
        conx= self.conexionBD()
        
        if(nom == "" or cor=="" or con == ""):
            messagebox.showwarning("aguas!, Revisa tu formulario")
            conx.close()
        else:
            cursor= conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,con)
            qrInser="insert into TbRegistrados(nombre,correo,contraseña) values(?,?,?)"
            
            cursor.execute(qrInser, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito"," Se guardo el Usuario")
            
    def encriptarCon(self,con):
        conplana= con
        conplana= conplana.encode()
        sel= bcrypt.gensalt()
    
    
    