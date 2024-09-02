import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class VistaD:
    def __init__(self, user_type):
        self.user_type = user_type
        self.idproducto = None
        self.nombre_producto = None
        self.precio = None
        self.cantidad = None
        self.ventana = None
        self.productos = [] 
        self.imagenes = {}   

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
                background=[('selected', "#40E0D0")],
                foreground=[('selected', 'turquoise')])

        frame_boton = tk.Frame(self.ventana, bg="turquoise")
        frame_boton.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(frame_boton, text="Registrar Producto", command=self.mostrar_datos_producto).pack(side=tk.LEFT, padx=5, pady=5)

        if self.user_type == "admin":
            tk.Button(frame_boton, text="Productos Más Vendidos", command=self.mostrar_productos_mas_vendidos).pack(side=tk.LEFT, padx=5, pady=5)
            tk.Button(frame_boton, text="Productos Menos Vendidos", command=self.mostrar_productos_menos_vendidos).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(frame_boton, text="Mostrar Todos los Productos", command=self.mostrar_todos_los_productos).pack(side=tk.LEFT, padx=5, pady=5)

        self.frame_contenido = tk.Frame(self.ventana, bg="turquoise")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.cargar_imagenes_predefinidas()

        self.mostrar_todos_los_productos()

        self.ventana.mainloop()

    def limpiar_frame_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def cargar_imagenes_predefinidas(self):
        imagenes_rutas = {
            '1': 'imagen1.jpg',  
            '2': 'imagen2.jpg',  
            '3': 'imagen3.jpg',  
            '4': 'imagen4.jpg',  
            '5': 'imagen5.jpg',  
            '6': 'imagen6.jpg',  
            '7': 'imagen7.jpg',  
            '8': 'imagen8.jpg',  
            '9': 'imagen9.jpg',  
            '10': 'imagen10.jpg' 
        }

        for producto_id, ruta in imagenes_rutas.items():
            if os.path.isfile(ruta):
                try:
                    imagen = Image.open(ruta)
                    imagen = imagen.resize((100, 100), Image.LANCZOS) 
                    self.imagenes[producto_id] = ImageTk.PhotoImage(imagen)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo cargar la imagen: {ruta}\n{e}")

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

        tk.Button(groobox, text="Guardar", width=10, command=self.obtener_datos).grid(row=4, column=0, padx=5, pady=10)
        tk.Button(groobox, text="Mostrar/Actualizar", width=15, command=self.cargar_datos).grid(row=4, column=1, padx=5, pady=10)

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

    def mostrar_todos_los_productos(self):
        self.limpiar_frame_contenido()

        groobox = tk.LabelFrame(self.frame_contenido, text='Todos los Productos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.tree_productos = ttk.Treeview(groobox, columns=('id', 'nombre', 'precio', 'cantidad'), show='headings', height=10)
        self.tree_productos.heading('#1', text="ID")
        self.tree_productos.heading('#2', text="Nombre")
        self.tree_productos.heading('#3', text="Precio")
        self.tree_productos.heading('#4', text="Cantidad")
        self.tree_productos.column('#1', anchor=tk.CENTER)
        self.tree_productos.column('#2', anchor=tk.CENTER)
        self.tree_productos.column('#3', anchor=tk.CENTER)
        self.tree_productos.column('#4', anchor=tk.CENTER)
        self.tree_productos.pack(fill=tk.BOTH, expand=True)

        for producto in self.productos:
            self.tree_productos.insert('', 'end', values=(producto['id'], producto['nombre'], producto['precio'], producto['cantidad']))

        self.frame_imagenes = tk.Frame(self.frame_contenido, bg='light grey')
        self.frame_imagenes.pack(fill=tk.X, padx=10, pady=10)

        self.mostrar_imagenes()

    def mostrar_imagenes(self):
        for widget in self.frame_imagenes.winfo_children():
            widget.destroy()

        for index, (producto_id, imagen_tk) in enumerate(self.imagenes.items()):
            row = index // 5
            column = index % 5
