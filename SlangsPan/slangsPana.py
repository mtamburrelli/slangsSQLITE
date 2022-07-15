from ast import Try
import sqlite3
from sqlite3 import Error
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH+'/slangs.db'

def crear_conexion(ruta):
    conn = None
    try:
        conn = sqlite3.connect(ruta)
        print("Conexión exitosa")
    except Error as e:
        print("Error:", e)
    return conn

def exe_consulta(conn, consulta):
    c = conn.cursor()
    try:
        c.execute(consulta)
        conn.commit()
        print("Consulta exitosa")
    except Error as e:
        print("Error:", e)


def viewSlang(conn, consulta):
    c=conn.cursor()
    try:
        c.execute(consulta)
        slangs = c.fetchone()
        print(slangs)
    except Error as e:
        print("Error:", e)

def viewSlangs(conn, consulta):
    c = conn.cursor()
    try:
        c.execute(consulta)
        slangs = c.fetchall()
        print(slangs)
    except Error as e:
        print("Error:", e)

def defineSlang(conn, consulta):
    c = conn.cursor()
    try:
        c.execute(consulta)
        fila = c.fetchone()
        print(fila)
    except Error as e:
        print("Error:", e)

def deleteSlang(conn, consulta):
    c = conn.cursor()
    try:
        c.execute(consulta)
        print(consulta)
    except Error as e:
        print("Error:", e)

def salir(conn):
    c = conn.cursor()
    c.close()


conn = sqlite3.connect(DB_PATH)

if __name__ == '__main__':
    crear_conexion(DB_PATH)

crearTabla = """CREATE TABLE SlangsPanameños (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    SLANG TEXT NOT NULL,
    DEFINICION TEXT NOT NULL
)
"""

deleteAll = "DROP TABLE SlangsPanameños"

selectAll = "SELECT * FROM SlangsPanameños"


exe_consulta(conn,crearTabla)


#exe_consulta(conn, deleteAll)



resp = input("¿Deseas agregar un slang? Y/N:\n")
if resp == 'Y' or resp == 'y':
    s = input("Slang:")
    d = input("Definición:")
    addSlang = """ INSERT INTO SlangsPanameños (SLANG, DEFINICION)
            VALUES ('{}','{}' );
            """.format(s, d)
    exe_consulta(conn, addSlang)
elif resp == 'n' or resp == 'N':
    print("Slangs:\n")
    viewSlangs(conn, selectAll)


viewSlangs(conn, selectAll)


id = input("¿Qué definición desea saber? (ID)\n")
id = int(id)
definicion = """
SELECT DEFINICION FROM SlangsPanameños WHERE
ID = {}
""".format(id)
defineSlang(conn, definicion)


resp = input("¿Deseas eliminar un slang? Y/N:\n")
if resp == 'Y' or resp == 'y':
    idd = input("¿Qué slang desea eliminar? (ID))\n")
    idd = int(idd)
    delSlang = "DELETE FROM SlangsPanameños WHERE ID = {} ;".format(idd)
    exe_consulta(conn, delSlang)
elif resp == 'n' or resp == 'N':
    print("Slangs:\n")
    viewSlangs(conn, selectAll)

resp = input("¿Deseas editar un slang? Y/N:\n")
if resp == 'Y' or resp == 'y':
    idd = input("¿Qué slang desea editar? (ID)\n")
    idd = int(idd)
    view = """SELECT SLANG, DEFINICION FROM SlangsPanameños WHERE
    ID = {}""".format(idd)
    viewSlangs(conn, view)
    d = input("Definicón: ")
    editSlang = """ UPDATE SlangsPanameños SET DEFINICION = '{}' WHERE ID = {}; """.format(d, idd)
    exe_consulta(conn, editSlang)
elif resp == 'n' or resp == 'N':
    print("Slangs:\n")
    viewSlangs(conn, selectAll)

viewSlangs(conn, selectAll)
salir(conn)

