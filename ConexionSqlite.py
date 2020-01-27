# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:15:53 2019

@author: Fire & Soft
"""

import sqlite3

class Conexion:
    
    def __init__(self):
        self.conexion = sqlite3.connect('ejemplo.db')

        # Creamos el cursor
        self.cursor = self.conexion.cursor()

        # Ahora crearemos una tabla de usuarios con nombres, edades y emails
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios " \
                       "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

        # Guardamos los cambios haciendo un commit
        self.conexion.commit()

        self.conexion.close()
        
        
    def insertar(self):
        self.conexion = sqlite3.connect('ejemplo.db')
        self.cursor = self.conexion.cursor()
        
        # Insertamos un registro en la tabla de usuarios
        self.cursor.execute("INSERT INTO usuarios VALUES " \
            "('Hector', 27, 'hector@ejemplo.com')")
        
        # Guardamos los cambios haciendo un commit
        self.conexion.commit()
        
        self.conexion.close()
        
    def consulta(self):
        self.conexion = sqlite3.connect('ejemplo.db')
        self.cursor = self.conexion.cursor()
        
        # Recuperamos los registros de la tabla de usuarios
        self.cursor.execute("SELECT * FROM usuarios")
        
        # Mostrar el cursos a ver que hay ?
        print(self.cursor)
        
        # Recorremos el primer registro con el método fetchone, devuelve una tupla
        usuario = self.cursor.fetchone()
        print(usuario)
        
        self.conexion.close()
        
    def insercionMultiple(self):
        self.conexion = sqlite3.connect('ejemplo.db')
        self.cursor = self.conexion.cursor()
        
        # Creamos una lista con varios usuarios
        usuarios = [('Mario', 51, 'mario@ejemplo.com'),
                    ('Mercedes', 38, 'mercedes@ejemplo.com'),
                    ('Juan', 19, 'juan@ejemplo.com')]
        
        # Ahora utilizamos el método executemany() para insertar varios
        self.cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)
        
        # Guardamos los cambios haciendo un commit
        self.conexion.commit()
        
        self.conexion.close()

    def consultaMultiple(self):
        self.conexion = sqlite3.connect('ejemplo.db')
        self.cursor = self.conexion.cursor()
        
        # Recuperamos los registros de la tabla de usuarios
        self.cursor.execute("SELECT * FROM usuarios")
        
        # Recorremos todos los registros con fetchall
        # y los volcamos en una lista de usuarios
        usuarios = self.cursor.fetchall()
        
        # Ahora podemos recorrer todos los usuarios
        for usuario in usuarios:
            print(usuario)
        
        self.conexion.close()
        
    
    def consultaWhere(self):
        self.conexion = sqlite3.connect('usuarios_autoincremental.db')
        self.cursor = self.conexion.cursor()
        
        # Recuperamos un registro de la tabla de usuarios
        self.cursor.execute("SELECT * FROM usuarios WHERE id=1")
        
        usuario = self.cursor.fetchone()
        print(usuario)
        
        self.conexion.close()
        
       
    def actualizar(self):
        self.conexion = sqlite3.connect('usuarios_autoincremental.db')
        self.cursor = self.conexion.cursor()
        
        # Actualizamos un registro
        self.cursor.execute("UPDATE usuarios SET nombre='Hector Costa' " \
            "WHERE dni='11111111A'")
        
        # Ahora lo consultamos de nuevo
        self.cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
        usuario = self.cursor.fetchone()
        print(usuario)
        
        self.conexion.commit()
        self.conexion.close()
    
        
    def borrar(self):
        self.conexion = sqlite3.connect('usuarios_autoincremental.db')
        self.cursor = self.conexion.cursor()
        
        # Creamos un registro de prueba
        self.cursor.execute("INSERT INTO usuarios VALUES " \
            "(null, '55555555E', 'Fernando', 31, 'fernando@ejemplo.com')")
        
        # Consultamos los usuarios
        for usuario in self.cursor.execute("SELECT * FROM usuarios"):
            print(usuario)
        
        # Ahora lo borramos
        self.cursor.execute("DELETE FROM usuarios WHERE dni='55555555E'")
        
        print() # Espacio en blanco
        
        # Consultamos de nuevo los usuarios
        for usuario in self.cursor.execute("SELECT * FROM usuarios"):
            print(usuario)
        
        self.conexion.commit()
        self.conexion.close()
