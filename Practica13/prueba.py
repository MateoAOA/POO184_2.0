import tkinter as tk
import string
import random
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self):
        # Configuración de la ventana
        self.root = tk.Tk()
        self.root.title("Generador de Contraseñas")
        self.root.geometry("300x250")

        # Variables
        self.length = tk.IntVar(value=8)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=False)
        self.password = tk.StringVar(value="")

        # Etiquetas
        tk.Label(self.root, text="Longitud:").grid(row=0, column=0, sticky="w")
        tk.Label(self.root, text="Incluir mayúsculas:").grid(row=1, column=0, sticky="w")
        tk.Label(self.root, text="Incluir caracteres especiales:").grid(row=2, column=0, sticky="w")
        tk.Label(self.root, text="Contraseña generada:").grid(row=4, column=0, sticky="w")

        # Campos de entrada
        tk.Entry(self.root, textvariable=self.length).grid(row=0, column=1)
        tk.Checkbutton(self.root, variable=self.include_uppercase).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(self.root, variable=self.include_special).grid(row=2, column=1, sticky="w")

        # Botones
        tk.Button(self.root, text="Generar contraseña", command=self.generate_password).grid(row=3, column=0, pady=10)
        tk.Button(self.root, text="Comprobar fortaleza", command=self.check_strength).grid(row=3, column=1, pady=10)

        # Campo de salida
        tk.Entry(self.root, textvariable=self.password, state="readonly").grid(row=4, column=1)

        # Iniciar aplicación
        self.root.mainloop()

    def generate_password(self):
        # Caracteres disponibles
        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_special.get():
            characters += string.punctuation

        # Generar contraseña
        password = "".join(random.choices(characters, k=self.length.get()))
        self.password.set(password)

    def check_strength(self):
        password = self.password.get()

        # Comprobar longitud
        length_score = min(2 * len(password) // self.length.get(), 2)
        
        # Comprobar uso de mayúsculas y minúsculas
        uppercase_score = any(c.isupper() for c in password) * 2
        
        # Comprobar uso de caracteres especiales
        special_score = any(c in string.punctuation for c in password) * 2
        
        # Calcular puntuación total
        strength_score = length_score + uppercase_score + special_score
        
        # Mostrar mensaje de fortaleza
        if strength_score < 3:
            message = "La contraseña es débil."
        elif strength_score < 5:
            message = "La contraseña es moderada."
        else:
            message = "La contraseña es fuerte."
        messagebox.showinfo("Fortaleza de la contraseña", message)

if __name__ == "__main__":
    PasswordGenerator()
