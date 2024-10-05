

from vistalogin import LoginApp
from conexion import conect
from reporte import Vista_reporte
from tkinter import messagebox


class Controlador:
    def __init__(self):
        #aqui estoy llamando la conexion de la base de datos
        self.objconexion = conect()
        #aqui esty llamando el login ya que esto me va permitir a la hora de validar el usuario y lleva self el login ya que la vista logien estoy llamando un paramtro controler en el cual me va permitir interactuar con el controlador
        self.objlogin = LoginApp(self)
        self.rol_actual = None

    # aqui cree una funcion en la cual la llame validacion de datos que interactua la vista login con el controlador y tambien estoy llamando el modelo para validar el rol usuario   

    def validarUsuario(self, usuario, contraseña):
        if usuario and contraseña:
            if self.objconexion.validar(usuario, contraseña):
                self.usuario_actual = usuario
                self.rol_actual = self.objconexion.rol_usuario(usuario)
                texto = "Bienvenido Usuario"

                self.abrir_vista_reporte()
               
               
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    #aqui cre una funcion en la que estoy llamando la vista de reporte en cual a la hora de validar el usuario me va entrar a la vista

    def abrir_vista_reporte(self):
        self.objreporte = Vista_reporte(self)
        self.objreporte.crearventana()

    # aqui me cree una funcion en la cual me va permitir registar los producto y llamo la conexion para a la hora de ingresar datos ya que esta conectada con la base de datos  

    def registrarProducto(self, idproducto, nombre_producto, precio, cantidad):
        self.objconexion.ingresar_datos(idproducto, nombre_producto, precio, cantidad)

    def tablaProductos(self):
        if hasattr(self, 'objvista'):
            fila = self.objconexion.consultarDatos()
            self.objreporte.infoProducto(fila)

    # aqui  me cree una funcion a la hora de modificar los productos y llamo conexion para valide la actualizacion en la base de datos       

    def modificarProducto(self, idproducto, nombre_producto, precio, cantidad):
        self.objconexion.modificar_datos(idproducto, nombre_producto, precio, cantidad)

    # aqui me cree una funcion de eliminar el producto que me va permitir la eliminacion del prodcuto que estoy llamando al modelo para que me esta validando

    def EliminacionProducto(self, idproducto):
        self.objconexion.eliminar_datos(idproducto)

    #aqui me cree una funcion  en la cual me va mostrar los producto mas vendidos y nmenos    

    def obtener_mas_vendidos(self):
        productos_mas_vendidos = self.objconexion.productos_mas_vendidos()
        
        return productos_mas_vendidos

    def obtener_menos_vendidos(self):
        productos_menos_vendidos = self.objconexion.productos_menos_vendidos()
        return productos_menos_vendidos   

    def ActualizarProductos(self):
        """Devuelve todos los productos disponibles."""
        return self.objconexion.consultarDatos()

# Crear instancias y configurar la aplicación
objcontrolador = Controlador()
