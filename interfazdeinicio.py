import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    credentials = {
        "giovanni": "1093743462",
        "jesus": "1090369704",
        "henry": "1090374464"
    }

    if credentials.get(username) == password:
        messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Inicio de sesión")

root.geometry("300x200")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor="center")

label_usuario = tk.Label(frame, text="Usuario", bg="lightblue")
label_usuario.grid(row=0, column=0, pady=10)

entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=1, column=0, pady=5)

label_password = tk.Label(frame, text="Contraseña", bg="lightblue")
label_password.grid(row=2, column=0, pady=10)

entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=3, column=0, pady=5)

button_login = tk.Button(frame, text="Iniciar sesión", command=login)
button_login.grid(row=4, column=0, pady=20)

root.mainloop()
