from mySQL_PYTHON import Mysqlconnect, Conexion, Error

class OlimpiadaMySql(Mysqlconnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.cursor = None

    def insertar(self, id, año):
        self.conectar()
        try:
            self.cursor = self.dbconexion.cursor()
            sql = "INSERT INTO olimpiada VALUES (%s, %s)"
            val = (id, año)
            self.cursor.execute(sql, val)
            self.dbconexion.commit()
            self.cursor.close()
            self.desconectar()
            print("Insercion de datos exitosa")
            return True

        except Error as e:
            self.desconectar()
            print(f"Error al agregar datos: {e}")
            return False

    def editar(self, año, nuevo_año):
        self.conectar()
        try:
            self.cursor = self.dbconexion.cursor()
            check_sql = "SELECT COUNT(*) FROM olimpiada WHERE year_olimpiada = %s"
            self.cursor.execute(check_sql, (nuevo_año,))
            count = self.cursor.fetchone()[0]

            if count > 0:
                print("El año que intentas editar ya se encuentra en la tabla.")
                self.cursor.close()
                self.desconectar()
                return False

            else:
                sql = "UPDATE olimpiada SET year_olimpiada = %s WHERE year_olimpiada = %s"
                val = (nuevo_año, año)
                self.cursor.execute(sql, val)
                self.dbconexion.commit()
                self.cursor.close()
                self.desconectar()
                print("Edicion de datos exitosa")
                return True

        except Error as e:
            self.desconectar()
            print(f"Error al editar datos: {e}")
            return False


if __name__ == "__main__":
    db = OlimpiadaMySql(Conexion.HOST.value, Conexion.USER.value, Conexion.PASSWORD.value, Conexion.DATABASE.value)
    #db.insertar(5, 2008)
    #db.editar(2008, 2000)
