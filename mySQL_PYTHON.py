from mysql.connector import connect, Error
import tkinter as tk
from tkinter import messagebox

class Mysqlconnect():
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self.dbconexion = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value

    def conectar(self):
        try:
            self.dbconexion = connect(
                host = self._host,
                user = self._user,
                password = self._password,
                database = self._database
            )
            tk.messagebox.showinfo(
                "Conexion abierta",
                f"Conexion abierta {self.dbconexion}\nTipo de conexión: {type(self.dbconexion)}"
            )


        except Error as e:
            print(e)

    def desconectar(self):
        self.dbconexion.close()
        tk.messagebox.showinfo("Conexion cerrada",
                               "Se ha cerrado la conexion con la base de datos")

if __name__ == "__main__":
    db = Mysqlconnect("localhost",
                      "root",
                      "AAAAAA", #CAMBIAR POR TU CONTRASEÑA
                      "olimpiadas")
    db.conectar()
    db.desconectar()