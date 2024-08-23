import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

class VistaD:
    def __init__(self):
        self.idproducto = None
        self.nombre_producto = None
        self.precio = None
        self.cantidad = None
        self.ventana = None
        self.imagen_path = None
        self.imagen_label = None

    def crearventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Productos")
        self.ventana.config(bg="turquoise")
        self.ventana.geometry("1200x800")

        style = ttk.Style()
        style.configure("Treeview",
                        background="#f0f0f0",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#f0f0f0")
        style.configure("Treeview.Heading",
                        background="#f0f0f0",
                        foreground="black",
                        relief="flat")
        style.map("Treeview",
                background=[('selected', "#4OEODO")],
                foreground=[('selected', 'turquoise')])

        frame_boton = tk.Frame(self.ventana, bg="turquoise")
        frame_boton.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(frame_boton, text="Registrar Producto", command=self.mostrar_datos_producto).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame_boton, text="Productos Más Vendidos", command=self.mostrar_productos_mas_vendidos).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame_boton, text="Productos Menos Vendidos", command=self.mostrar_productos_menos_vendidos).pack(side=tk.LEFT, padx=5, pady=5)

        self.frame_contenido = tk.Frame(self.ventana, bg="turquoise")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.mostrar_datos_producto()

        self.ventana.mainloop()

    def limpiar_frame_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_datos_producto(self):
        self.limpiar_frame_contenido()

        groobox = tk.LabelFrame(self.frame_contenido, text='Datos del Producto', padx=30, pady=10, bg='deep sky blue', width=1150, height=250)
        groobox.pack(padx=10, pady=10)

        tk.Label(groobox, text="ID Producto", width=20).grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.idproducto = tk.Entry(groobox, width=30)
        self.idproducto.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(groobox, text="Nombre Producto", width=20).grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.nombre_producto = tk.Entry(groobox, width=30)
        self.nombre_producto.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(groobox, text="Precio", width=20).grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.precio = tk.Entry(groobox, width=30)
        self.precio.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(groobox, text="Cantidad", width=20).grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.cantidad = tk.Entry(groobox, width=30)
        self.cantidad.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(groobox, text="Cargar Imagen", command=self.cargar_imagen).grid(row=4, column=0, padx=5, pady=10)

        self.imagen_label = tk.Label(groobox, bg='white', width=100, height=20)
        self.imagen_label.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(groobox, text="Guardar", width=10, command=self.obtener_datos).grid(row=5, column=0, padx=5, pady=10)
        tk.Button(groobox, text="Mostrar/Actualizar", width=15, command=self.cargar_datos).grid(row=5, column=1, padx=5, pady=10)

    def cargar_imagen(self):
        archivo = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if archivo:
            self.imagen_path = archivo
            imagen = Image.open(archivo)
            imagen = imagen.resize((200, 200), Image.ANTIALIAS)
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.imagen_label.config(image=self.imagen_tk)
            self.imagen_label.image = self.imagen_tk  

    def mostrar_productos_mas_vendidos(self):
        self.limpiar_frame_contenido()

        groobox = tk.LabelFrame(self.frame_contenido, text='Productos Más Vendidos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.car = ttk.Treeview(groobox, columns=('id', 'nombre', 'total_vendido'), show='headings', height=25)
        self.car.heading('#1', text="ID")
        self.car.heading('#2', text="Nombre")
        self.car.heading('#3', text="Total Vendido")
        self.car.column('#1', anchor=tk.CENTER)
        self.car.column('#2', anchor=tk.CENTER)
        self.car.column('#3', anchor=tk.CENTER)
        self.car.pack(fill=tk.BOTH, expand=True)

    def mostrar_productos_menos_vendidos(self):
        self.limpiar_frame_contenido()

        groobox = tk.LabelFrame(self.frame_contenido, text='Productos Menos Vendidos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.tree_productos_vendidos = ttk.Treeview(groobox, columns=('id', 'nombre', 'total_vendido'), show='headings', height=25)
        self.tree_productos_vendidos.heading('#1', text="ID")
        self.tree_productos_vendidos.heading('#2', text="Nombre")
        self.tree_productos_vendidos.heading('#3', text="Total Vendido")
        self.tree_productos_vendidos.column('#1', anchor=tk.CENTER)
        self.tree_productos_vendidos.column('#2', anchor=tk.CENTER)
        self.tree_productos_vendidos.column('#3', anchor=tk.CENTER)
        self.tree_productos_vendidos.pack(fill=tk.BOTH, expand=True)

    def obtener_datos(self):
        pass

    def cargar_datos(self):
        pass

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inicio de sesión")
        self.root.geometry("300x200")
        self.root.configure(bg="lightblue")

        self.frame = tk.Frame(self.root, bg="lightblue")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="Usuario", bg="lightblue").grid(row=0, column=0, pady=10)
        self.entry_username = tk.Entry(self.frame)
        self.entry_username.grid(row=1, column=0, pady=5)

        tk.Label(self.frame, text="Contraseña", bg="lightblue").grid(row=2, column=0, pady=10)
        self.entry_password = tk.Entry(self.frame, show="*")
        self.entry_password.grid(row=3, column=0, pady=5)

        tk.Button(self.frame, text="Iniciar sesión", command=self.login).grid(row=4, column=0, pady=20)

        self.root.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        credentials = {
            "giovanni": "1093743462",
            "jesus": "1090369704",
            "henry": "1090374464"
        }

        if credentials.get(username) == password:
            self.root.destroy()
            self.abrir_ventana_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def abrir_ventana_principal(self):
        vista = VistaD()
        vista.crearventana()

if __name__ == "__main__":
    app = LoginApp()
