from conexion import*
class modelot:
    def __init__(self):
        self.idproducto=None
        self.nombre_producto=None
        self.precio=None
        self.cantidad=None

    def get_ide(self):
        return self.idproducto
    def get_nombre(self):
        return self.nombre_producto
    def get_precio(self):
        return self.precio
    def get_cantidad(self):
        return self.cantida    

    def set_ideproducto(self,datoid):
        self.idproducto=datoid

    def set_nombre_producto(self,datonombre):
        self.nombre_producto=datonombre

    def set_precio(self,datoprecio):
        self.precio=datoprecio
    def set_cantida(self,datocantida):
        self.cantida=datocantida

    def mostrardatos(self):
        try:
            cone=conector.conexion_basedatos()
            cursor=cone.cursor()
            cursor.execute( "select * from formulario;")
            miresultado=cursor.fetchall()#fetchall es para que me meustre todo
            cone.commit()
            cone.close()
            return miresultado

        except mysql.connector.Error as error:
            print('error ingreso de datos {}'.format(error)) 

    def ingresar_datos(self,idproducto,nombre_producto,precio,cantidad):
        try:
            cone=conector.conexion_basedatos() 
            curs=cone.cursor() #esta variable va ejecurtar la conexion
            ql="insert into registro values(%s,%s,%s,%s);"
            valores=(idproducto,nombre_producto,precio,cantidad)
            curs.execute(ql,valores) #aqui estoy uniendo cada parametro en su respectivo padre
            cone.commit()
            print(curs.rowcount,'registro ingresado')

        except mysql.connector.Error as error:
            print("error a la hora de mostrar datos {}".format(error))

    def formato_json(self):
         return f"{self.get_ide()}, {self.get_nombre()}, {self.get_precio()}, {self.get_cantidad()}"
    def guardar_archivo(self,archivo="archivo.json"):
        datos=self.formato_json()
        with open(archivo,"a") as linea:
            linea.write(datos + "\n")


    def mostrardatos_usuario(self):
        try:
            cone=conector.conexion_basedatos()
            cursor=cone.cursor()
            cursor.execute( "select * from usuario;")
            miresultado=cursor.fetchall()
            cone.commit()
            cone.close()
            return miresultado

        except mysql.connector.Error as error:
            print('error ingreso de datos {}'.format(error))  

    def ingresar_datos_usuario(self,nombre,contraseña):
        try:
            cone=conector.conexion_basedatos() 
            curs=cone.cursor() 
            ql="insert into usuario value(%s,%s); "
            valores=(nombre,contraseña)
            curs.execute(ql,valores) 
            cone.commit()
            print(curs.rowcount,'registro ingresado')

        except mysql.connector.Error as error:
            print("error a la hora de mostrar datos {}".format(error))
              

             

   










