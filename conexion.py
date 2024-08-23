import mysql.connector
class conexion:
    def conector_base_datos():
        try:
            conecto=mysql.connector.connect(user='root',password='jesus123',host='127.0.0.1',database='catalago',port='3306')
            print("conexion correcta")
        except mysql.connector.Error as error:
            print("al error al conectar a la base de datos {}".format(error))
            return conecto
    conector_base_datos()    
