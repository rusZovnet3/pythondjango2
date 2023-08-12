print("\n==========  Herencia Multiple  ====================\n")

class desarrollador:
    def categoria(self):
        print("categoria Junior")

    def asignatura(self):
        print("desarrollo Desktop")

class sistemaOperativo:
    def operativo(self):
        print("sistema Operativo MacOx")
        
    def versiones(self):
        print("15874Mb")
        
class etapaDesarrollo(self):
    def especialista(self):
        print("area del backend")
        
    def metodologia(delf):
        print("metodología Scrum")
        
class lenguajeProgramacion:
    def javascript(self):
        print("Programando Javascript")
        
    def python(self):
        print("Programando Pythón")
        
    def appserv(self):
        print("Programando Php 8")

class Carrera:
    
    def docentes(self):
        print("Carmen Evelin Estrada")
        
    def horario(self):
        print("Lunes: 10:00 - 12:00")
        
    def asignatura(self):
        print("Ing en Sistemas")
    

class Materia:
    
    def asignatura(self):
        print("Base de Datos II")
        
    def credito(self):
        print("tiene 5 creditos")
        


#class Especialidad(Materia, Carrera):       # Herencia Multiple
#class Especialidad(Carrera, Materia):   
class Especialidad(etapaDesarrollo, Materia):  
    def modulos(self):
        print("Administracion Avanzadas de Bases de Datos")
        
    def costo(self):
        print("Matricula minimo Bs. 3000")


# las funciones ambiguas de la clase, 
# Busca del parametro herencia de izquierda y lo reemplaza a la derecha


""" obj1 = Especialidad()
obj1.asignatura() """



