if __name__ != "__main__":
    
    #from ..gestion.crud import guardar     #  import relativo
    
    from usuarios.gestion.crud import guardar   # import absoluto

    print(__name__)   # nombre de la ruta del archivo actual


    def pagar_impuesto():
        print("pagando impuestos.....!, espere....")
        guardar()
    
if __name__ == "__main__":
    print("Mucha tarea de mantenimiento. utilidades.")
