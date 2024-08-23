from tkinter import *
from tkinter import ttk

class VistaD:
    def __init__(self):
        self.idproducto = None
        self.nombre_producto = None
        self.precio = None
        self.cantidad = None
        self.ventana = None

    def crearventana(self):
        self.ventana = Tk()
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

        frame_boton = Frame(self.ventana, bg="turquoise")
        frame_boton.pack(fill=X, padx=10, pady=10)

        Button(frame_boton, text="Datos del Producto", command=self.mostrar_datos_producto).pack(side=LEFT, padx=5, pady=5)
        Button(frame_boton, text="Productos Más Vendidos", command=self.mostrar_productos_mas_vendidos).pack(side=LEFT, padx=5, pady=5)
        Button(frame_boton, text="Productos Menos Vendidos", command=self.mostrar_productos_menos_vendidos).pack(side=LEFT, padx=5, pady=5)

        self.frame_contenido = Frame(self.ventana, bg="turquoise")
        self.frame_contenido.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.mostrar_datos_producto()

        self.ventana.mainloop()

    def limpiar_frame_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_datos_producto(self):
        self.limpiar_frame_contenido()

        groobox = LabelFrame(self.frame_contenido, text='Datos del Producto', padx=30, pady=10, bg='deep sky blue', width=1150, height=250)
        groobox.pack(padx=10, pady=10)

        Label(groobox, text="ID Producto", width=20).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.idproducto = Entry(groobox, width=30)
        self.idproducto.grid(row=0, column=1, padx=10, pady=10)

        Label(groobox, text="Nombre Producto", width=20).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.nombre_producto = Entry(groobox, width=30)
        self.nombre_producto.grid(row=1, column=1, padx=10, pady=10)

        Label(groobox, text="Precio", width=20).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.precio = Entry(groobox, width=30)
        self.precio.grid(row=2, column=1, padx=10, pady=10)

        Label(groobox, text="Cantidad", width=20).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.cantidad = Entry(groobox, width=30)
        self.cantidad.grid(row=3, column=1, padx=10, pady=10)

        Button(groobox, text="Guardar", width=10, command=self.obtener_datos).grid(row=4, column=0, padx=5, pady=10)
        Button(groobox, text="Mostrar/Actualizar", width=15, command=self.cargar_datos).grid(row=4, column=1, padx=5, pady=10)

    def mostrar_productos_mas_vendidos(self):
        self.limpiar_frame_contenido()

        groobox = LabelFrame(self.frame_contenido, text='Productos Más Vendidos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.car = ttk.Treeview(groobox, columns=('id', 'nombre', 'total_vendido'), show='headings', height=25)
        self.car.heading('#1', text="ID")
        self.car.heading('#2', text="Nombre")
        self.car.heading('#3', text="Total Vendido")
        self.car.column('#1', anchor=CENTER)
        self.car.column('#2', anchor=CENTER)
        self.car.column('#3', anchor=CENTER)
        self.car.pack(fill=BOTH, expand=True)

    def mostrar_productos_menos_vendidos(self):
        self.limpiar_frame_contenido()

        groobox = LabelFrame(self.frame_contenido, text='Productos Menos Vendidos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.tree_productos_vendidos = ttk.Treeview(groobox, columns=('id', 'nombre', 'total_vendido'), show='headings', height=25)
        self.tree_productos_vendidos.heading('#1', text="ID")
        self.tree_productos_vendidos.heading('#2', text="Nombre")
        self.tree_productos_vendidos.heading('#3', text="Total Vendido")
        self.tree_productos_vendidos.column('#1', anchor=CENTER)
        self.tree_productos_vendidos.column('#2', anchor=CENTER)
        self.tree_productos_vendidos.column('#3', anchor=CENTER)
        self.tree_productos_vendidos.pack(fill=BOTH, expand=True)

    def obtener_datos(self):
        pass

    def cargar_datos(self):
        pass

vista = VistaD()
vista.crearventana()
