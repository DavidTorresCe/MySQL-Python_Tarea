from mySQL_PYTHON import Mysqlconnect, Conexion, Error

class ResultadosMySql(Mysqlconnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.cursor = None

    def insertar(self, idolimpiada, idpais, idgenero, oro, plata, bronce):
        self.conectar()

        try:
            self.cursor = self.dbconexion.cursor()
            sql = "INSERT INTO resultados VALUES (%s, %s, %s, %s, %s, %s)"
            val = (idolimpiada, idpais, idgenero, oro, plata, bronce)
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

    def editar(self, olimp, pais, genr, oro, plata, bronce):
        self.conectar()
        try:
            self.cursor = self.dbconexion.cursor()
            if any(x < 0 for x in (oro, plata, bronce)):
                print("El número de medallas debe ser positivo")
                self.desconectar()
                return False
            else:
                sql = "UPDATE Resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
                val = (oro, plata, bronce, olimp, pais, genr)
                self.cursor.execute(sql, val)
                self.dbconexion.commit()
                self.cursor.close()
                self.desconectar()
                print("Edición de datos exitosa")
                return True
        except Error as e:
            self.desconectar()
            print(f"Error al editar datos: {e}")
            return False


if __name__ == "__main__":
    db = ResultadosMySql(Conexion.HOST.value, Conexion.USER.value, Conexion.PASSWORD.value, Conexion.DATABASE.value)
    #db.insertar(2, 3, 2, 4, 1, 2)
    #db.editar(1, 1, 1, 1, 2, 90)