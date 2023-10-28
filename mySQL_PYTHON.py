from mysql.connector import connect, Error
import tkinter as tk
from tkinter import messagebox
from enum import Enum

class Conexion(Enum):
    HOST = "localhost"
    USER = "root"
    PASSWORD = "Ab@ntonio347"  # Cambia esto a tu contraseña
    DATABASE = "olimpiadas"

class Mysqlconnect():
    def __init__(self, host, user, password, database):
        self._host = Conexion.HOST.value
        self._user = Conexion.USER.value
        self._password = Conexion.PASSWORD.value
        self._database = Conexion.DATABASE.value
        self.dbconexion = None

    def conectar(self):
        try:
            self.dbconexion = connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )

            tk.messagebox.showinfo(
                "Conexion abierta",
                f"Conexion abierta\nTipo de conexión: {type(self.dbconexion)}"
            )

        except Error as e:
            print(e)

    def desconectar(self):
        if self.dbconexion is not None:
            self.dbconexion.close()
            tk.messagebox.showinfo("Conexion cerrada", "Se ha cerrado la conexión con la base de datos")

if __name__ == "__main__":
    db = Mysqlconnect(Conexion.HOST.value, Conexion.USER.value, Conexion.PASSWORD.value, Conexion.DATABASE.value)
    db.conectar()
    db.desconectar()
