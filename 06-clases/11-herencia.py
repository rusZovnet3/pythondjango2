print("\n==========  Herencia  ====================\n")

class Carrera:

    def docentes(self):
        print("Carmen Evelin")

    def horario(self):
        print("Lunes: 10:00 - 12:00")


class Materia(Carrera):         # Herencia

    def asignatura(self):
        print("Base de Datos II")

    def credito(self):
        print("tiene 5 creditos")



class Especialidad(Materia):    # Herencia Multinivel

    def modulos(self):
        print("Administracion Avanzadas de Bases de Datos")

obj1 = Materia()
obj1.docentes()