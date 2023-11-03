"""
Torres Celedon David Antonio 951 2/NOV/23

Desarrollar una clase llamada MySQLConnect que tenga como atributos:
host, user, password, database. Debe crear sus métodos set y get (property, setters).
Debe tener los siguientes métodos:
conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().

"""


from mysql.connector import connect, Error
#import tkinter as tk
#from tkinter import messagebox
from enum import Enum

class Conexion(Enum):
    HOST = "localhost"
    USER = "root"
    PASSWORD = "AAAAAA"  # Cambia esto a tu contraseña
    DATABASE = "olimpiadas"

class Mysqlconnect():
    def __init__(self, host, user, password, database):
        self._host = Conexion.HOST.value
        self._user = Conexion.USER.value
        self._password = Conexion.PASSWORD.value
        self._database = Conexion.DATABASE.value
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
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )

            print(
                f"Conexion abierta\nTipo de conexión: {type(self.dbconexion)}"
            )

        except Error as e:
            print(e)

    def desconectar(self):
        if self.dbconexion is not None:
            self.dbconexion.close()
            print("Se ha cerrado la conexión con la base de datos")

if __name__ == "__main__":
    db = Mysqlconnect(Conexion.HOST.value, Conexion.USER.value, Conexion.PASSWORD.value, Conexion.DATABASE.value)
    db.conectar()
    db.desconectar()
