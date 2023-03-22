from tkinter import messagebox, 
import inicio

def __init__(self):
    self.length = tk.IntVar(value=8)
    self.include_uppercase = tk.BooleanVar(value=True)
    self.include_special = tk.BooleanVar(value=False)
    self.password = tk.StringVar(value="")


def generar_password(self):
        # Caracteres disponibles
        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_special.get():
            characters += string.punctuation

        # Generar contraseña
        password = "".join(random.choices(characters, k=self.length.get()))
        self.password.set(password)

    def checar_password(self):
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
        