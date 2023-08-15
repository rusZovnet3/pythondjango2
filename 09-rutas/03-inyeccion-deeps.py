

print("\n===================  Inyeccion de Dependencias  =======================\n")

""" import Correa

class Perro:
    def __init__(self):
        self.correa = Correa() """
        
        
""" class Perro:
    def __init__(self, Correa):
        self.correa = Correa() """
        
        
""" import usuario

def guardar():
    usuario.guardar()               # sin inyeccion de dependencia
    
def guardar(entidad):
    entidad.guardar()               # Inyeccion de dependencia """
 
 
""" def init_app(bbdd, api): """
 
 
 # Practica, carpeta uno y dos --------------------
 
from pathlib import Path
import db
import graphql
import api

 
path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]  # sí es un directorio


""" dependencias = {
    "db": "Base de datos",
    "api": "esta es la Api",
    "graphql": "esto es un graphql"
} """


dependencias = {
    "db": db,
    "api": api,
    "graphql": graphql
}

def load(p):
    """ paquete = __import__(str(p).replace("/", "."))    # todas carpetas
    paquete.init()    # las carpetas que tengan la funcion """

    paquete = __import__(str(p).replace("/", "."))
    
    try:
        paquete.init(**dependencias)    # operador de enpaquetamiento
    except:
        print("El Paquete no tiene funcion init")       # carpeta folder, no tiene el archivo con la funcion
 
list(map(load, paths))
 
 

 
 
        