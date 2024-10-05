import mysql.connector

class conect:
    @staticmethod
    def conexion_basedatos():
        try:
            conet = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='registroproducto', port='33065')
            print("Conexión correcta")
            return conet
        except mysql.connector.Error as error:
            print(f"Error a la hora de conectar: {error}")
            return None
      
        


 
    
    @staticmethod 
    def validar(usuario, contraseña):
        conexion1 = conect.conexion_basedatos()
        if conexion1 is None:
            return False
        cursor = conexion1.cursor(dictionary=True)
        sql = "SELECT * FROM roles WHERE nombre = %s AND contraseña = %s"
        cursor.execute(sql, (usuario, contraseña))
        ContraseñaConsulta = cursor.fetchone()
        cursor.close()
        conexion1.close()
        return ContraseñaConsulta is not None



    @staticmethod  
    def rol_usuario( usuario):
        try:
            cone = conect.conexion_basedatos()
            if cone is None:
                return []
            cursor = cone.cursor()
            
            cursor.execute("SELECT rol FROM roles WHERE roles = %s", (usuario))
            rol=cursor.fetchall()
            cursor.close()
            cone.close()
            return rol
        except mysql.connector.Error as error:
            print(f"Error al mostrar datos: {error}")
            return []  





    @staticmethod
    def consultarDatos():
        try:
            cone = conect.conexion_basedatos()
            if cone is None:
                return []
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM catalago;") 
            miresultado = cursor.fetchall()
            cone.close()
            return miresultado
        except mysql.connector.Error as error:
            print(f"Error al mostrar datos: {error}")
            return []

    @staticmethod
    def ingresar_datos(idproducto, nombre_producto, precio, cantidad):
        try:
            cone = conect.conexion_basedatos()
            if cone is None:
                return
            curs = cone.cursor()
            ql = "INSERT INTO catalago (idproducto, nombre_producto, precio, cantidad) VALUES (%s, %s, %s, %s);"
            valores = (idproducto, nombre_producto, precio, cantidad)
            curs.execute(ql, valores)
            cone.commit()
            print(f'{curs.rowcount} registro(s) ingresado(s)')
        except mysql.connector.Error as error:
            print(f"Error al ingresar datos: {error}")
        finally:
            if cone:
                cone.close()

    @staticmethod
    def modificar_datos(idproducto, nombre_producto, precio, cantidad):
        try:
            cone = conect.conexion_basedatos()
            cursor = cone.cursor()
            ql = "UPDATE catalago SET nombre_producto=%s, precio=%s, cantidad=%s WHERE idproducto=%s;"
            valores = (nombre_producto, precio, cantidad, idproducto)
            cursor.execute(ql, valores)
            cone.commit()
        except mysql.connector.Error as error:
            print(f'Error al modificar datos: {error}')
        finally:
            if cone:
                cone.close()
    @staticmethod
    def eliminar_datos(idproducto):
        try:
            cone = conect.conexion_basedatos()
            if cone is None:
                return
            cursor = cone.cursor()
            ql = "DELETE FROM catalago WHERE idproducto=%s;"
            valores = (idproducto,)
            cursor.execute(ql, valores)
            cone.commit()
            print(f'{cursor.rowcount} registro(s) eliminado(s)')
        except mysql.connector.Error as error:
            print(f'Error al eliminar datos: {error}')
        finally:
            if cone:
                cone.close()

    @staticmethod
    def productos_mas_vendidos():
        cona = conect.conexion_basedatos()
        cursor = cona.cursor()
        qury ="SELECT nombre_producto, cantidad FROM catalago ORDER BY cantidad DESC LIMIT 3;"
        cursor.execute(qury)
        resultados = cursor.fetchall()
        cursor.close()
        cona.close()
        return resultados
    
    @staticmethod
    def productos_menos_vendidos():
        cona = conect.conexion_basedatos()
        cursor = cona.cursor()
        qury ="SELECT nombre_producto, cantidad FROM catalago ORDER BY cantidad ASC LIMIT 3;"
        cursor.execute(qury)
        resultados = cursor.fetchall()
        cursor.close()
        cona.close()
        return resultados
    

    
