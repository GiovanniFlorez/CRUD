import os
import tkinter as tk
from tkinter import ttk, messagebox

class Vista_reporte:
    def __init__(self, controller):
        self.controller = controller
        self.idproducto = None
        self.nombre_producto = None
        self.precio = None
        self.cantidad = None
        self.ventana = None
        self.productos = []

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
        tk.Button(frame_boton, text="Mostrar Todos los Productos", command=self.mostrar_todos_los_productos).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame_boton, text="Productos Más Vendidos", command=self.mostrar_productos_mas_vendidos).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame_boton, text="Productos Menos Vendidos", command=self.mostrar_productos_menos_vendidos).pack(side=tk.LEFT, padx=5, pady=5)

        self.frame_contenido = tk.Frame(self.ventana, bg="turquoise")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.mostrar_todos_los_productos()
        self.ventana.mainloop()

    def limpiar_frame_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_datos_producto(self):
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

        tk.Button(groobox, text="Guardar", width=15, command=self.guardar_datos).grid(row=4, column=0, padx=5, pady=10)
        tk.Button(groobox, text="Modificar", width=15, command=self.modifica_datos).grid(row=4, column=1, padx=5, pady=10)
        tk.Button(groobox, text="Eliminar", width=15, command=self.eliminarProducto).grid(row=4, column=2, padx=5, pady=10)
        tk.Button(groobox, text="txt", width=15, command=self.exportar_datos_a_txt).grid(row=4, column=3, padx=5, pady=10)

    def mostrar_productos_mas_vendidos(self):
        self.limpiar_frame_contenido()
        groobox = tk.LabelFrame(self.frame_contenido, text='Productos Más Vendidos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.tree_productos = ttk.Treeview(groobox, columns=('nombre', 'total_vendido'), show='headings', height=25)
        self.tree_productos.heading('#1', text="Nombre")
        self.tree_productos.heading('#2', text="Total Vendido")
        self.tree_productos.column('#1', anchor=tk.CENTER)
        self.tree_productos.column('#2', anchor=tk.CENTER)
        self.tree_productos.pack(fill=tk.BOTH, expand=True)

        productos = self.controller.obtener_mas_vendidos()
        for producto in productos:
            self.tree_productos.insert("", tk.END, values=producto)

    def mostrar_productos_menos_vendidos(self):
        self.limpiar_frame_contenido()
        groobox = tk.LabelFrame(self.frame_contenido, text='Productos Menos Vendidos', padx=5, pady=10, bg='deep sky blue', width=1150, height=600)
        groobox.pack(padx=10, pady=10)

        self.tree_productos_vendidos = ttk.Treeview(groobox, columns=('nombre', 'total_vendido'), show='headings', height=25)
        self.tree_productos_vendidos.heading('#1', text="Nombre")
        self.tree_productos_vendidos.heading('#2', text="Total Vendido")
        self.tree_productos_vendidos.column('#1', anchor=tk.CENTER)
        self.tree_productos_vendidos.column('#2', anchor=tk.CENTER)
        self.tree_productos_vendidos.pack(fill=tk.BOTH, expand=True)

        productos = self.controller.obtener_menos_vendidos()
        for producto in productos:
            self.tree_productos_vendidos.insert("", tk.END, values=producto)

    def mostrar_todos_los_productos(self):
        self.limpiar_frame_contenido()
        groobox = tk.LabelFrame(self.frame_contenido, text='Todos los Productos', padx=5, pady=10, bg='deep sky blue', width=1150)
        groobox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Obtener los datos de los productos
        productos = self.controller.ActualizarProductos()

        for producto in productos:
            frame_producto = tk.Frame(groobox, bg='light blue', padx=10, pady=10)
            frame_producto.pack(side=tk.LEFT, padx=5, pady=5)

            # Espacio para la imagen del producto (placeholder)
            label_imagen = tk.Label(frame_producto, text="Imagen", bg='light blue', width=10, height=5)  # Placeholder para la imagen
            label_imagen.pack(pady=5)

            # Mostrar detalles del producto
            tk.Label(frame_producto, text=f"ID: {producto[0]}", bg='light blue').pack()
            tk.Label(frame_producto, text=f"Nombre: {producto[1]}", bg='light blue').pack()
            tk.Label(frame_producto, text=f"Precio: {producto[2]}", bg='light blue').pack()
            tk.Label(frame_producto, text=f"Cantidad: {producto[3]}", bg='light blue').pack()

            # Al hacer clic en el frame del producto, se seleccionará
            frame_producto.bind('<Button-1>', lambda event, p=producto: self.seleccionar_producto(p))

    def seleccionar_producto(self, producto):
        self.idproducto.delete(0, "end")
        self.idproducto.insert(0, producto[0])
        self.nombre_producto.delete(0, "end")
        self.nombre_producto.insert(0, producto[1])
        self.precio.delete(0, "end")
        self.precio.insert(0, producto[2])
        self.cantidad.delete(0, "end")
        self.cantidad.insert(0, producto[3])

    def seleccionar(self, event):
        seleccion = self.tree_productos.focus()
        if seleccion:
            values = self.tree_productos.item(seleccion)["values"]
            self.idproducto.delete(0, "end")
            self.idproducto.insert(0, values[0])
            self.nombre_producto.delete(0, "end")
            self.nombre_producto.insert(0, values[1])
            self.precio.delete(0, "end")
            self.precio.insert(0, values[2])
            self.cantidad.delete(0, "end")
            self.cantidad.insert(0, values[3])

    def vaciar_tabla(self):
        filas = self.tree_productos.get_children()
        for fila in filas:
            self.tree_productos.delete(fila)

    def infoProducto(self, filas):
        for fila in filas:
            self.tree_productos.insert("", tk.END, values=fila)

    def guardar_datos(self):
        idproducto = self.idproducto.get()
        nombre_producto = self.nombre_producto.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        try:
            self.controller.registrarProducto(idproducto, nombre_producto, precio, cantidad)
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.limpiar_campos()
            self.mostrar_todos_los_productos()  # Refresh the product list
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar el producto: {e}")

    def modifica_datos(self):
        idproducto = self.idproducto.get()
        nombre_producto = self.nombre_producto.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        try:
            self.controller.modificarProducto(idproducto, nombre_producto, precio, cantidad)
            messagebox.showinfo("Éxito", "Producto modificado correctamente.")
            self.limpiar_campos()
            self.mostrar_todos_los_productos()  # Refresh the product list
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar el producto: {e}")

    def eliminarProducto(self):
        seleccion = self.tree_productos.focus()
        if not seleccion:
            messagebox.showerror("Error", "No se ha seleccionado ningún registro")
            return

        values = self.tree_productos.item(seleccion)["values"]
        idproducto = values[0]

        try:
            self.controller.EliminacionProducto(idproducto)
            self.tree_productos.delete(seleccion)  # Eliminar el registro de la tabla
            self.limpiar_campos()  # Limpiar los campos del formulario
            messagebox.showinfo("Acción Realizada Exitosamente", "Producto eliminado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el producto: {e}")

    def limpiar_campos(self):
        self.idproducto.delete(0, tk.END)
        self.nombre_producto.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)

    def exportar_datos_a_txt(self):
        try:
            datos = self.controller.ActualizarProductos()
            with open("productos.txt", "w") as file:
                for row in datos:
                    file.write(f"ID: {row[0]}, Nombre: {row[1]}, Precio: {row[2]}, Cantidad: {row[3]}\n")
            messagebox.showinfo('Información', 'Datos exportados a productos.txt')
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error al exportar los datos: {e}')
