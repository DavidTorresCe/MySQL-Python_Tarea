from mySQL_PYTHON import Mysqlconnect, Conexion, Error

class PaisMysql(Mysqlconnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.cursor = None

    def insertar(self, id, nombre):
        self.conectar()
        try:
            self.cursor = self.dbconexion.cursor()
            sql = "INSERT INTO pais (id, nombre) VALUES (%s, %s)"
            val = (id, nombre)
            self.cursor.execute(sql, val)
            self.dbconexion.commit()
            self.cursor.close()
            self.desconectar()
            return True

        except Error as e:
            self.desconectar()
            print(f"Error al agregar datos: {e}")
            return False

    def editar(self, nombre, nuevo_nombre):
        self.conectar()
        try:
            self.cursor = self.dbconexion.cursor()  # Crea un cursor al conectarse
            check_sql = "SELECT COUNT(*) FROM pais WHERE nombre = %s"
            self.cursor.execute(check_sql, (nuevo_nombre,))
            count = self.cursor.fetchone()[0]

            if count > 0:
                print("El nuevo nombre ya existe en la tabla.")
                self.cursor.close()
                self.desconectar()
                return False


            else:
                sql = "UPDATE pais SET nombre = %s WHERE nombre = %s"
                val = (nuevo_nombre, nombre)
                self.cursor.execute(sql, val)
                self.dbconexion.commit()
                self.cursor.close()
                self.desconectar()
                return True

        except Error as e:
            self.desconectar()
            print(f"Error al editar datos: {e}")
            return False

if __name__ == "__main__":
    db = PaisMysql(Conexion.HOST.value, Conexion.USER.value, Conexion.PASSWORD.value, Conexion.DATABASE.value)
    #db.insertar(3, "Marruecos")
    db.editar("Mexico", "USA")