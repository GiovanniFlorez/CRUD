from tkinter import*

import tkinter as tk

from tkinter import  messagebox



class LoginApp:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.title("Inicio de sesión")
        self.root.geometry("300x200")
        self.root.configure(bg="lightblue")
        self.controlador = controller

        self.frame = tk.Frame(self.root, bg="lightblue")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.labelNombre = tk.Label(self.frame, text="Usuario", bg="lightblue")
        self.labelNombre.grid(row=0, column=0, pady=10)
        self.entry_username = tk.Entry(self.frame)
        self.entry_username.grid(row=1, column=0, pady=5)

        self.labelContraseña = tk.Label(self.frame, text="Contraseña", bg="lightblue")
        self.labelContraseña.grid(row=2, column=0, pady=10)
        self.entry_password = tk.Entry(self.frame, show="*")
        self.entry_password.grid(row=3, column=0, pady=5)

        tk.Button(self.frame, text="Iniciar sesión", command=self.login).grid(row=4, column=0, pady=20)

        self.root.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controlador.validarUsuario(username, password)

    

    def Limpiar_login(self, texto):
        messagebox.showerror("ERROR DE INGRESO", texto)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    