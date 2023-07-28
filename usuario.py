from data import DataJson

class Usuario:
    def __init__(self, id, nombre, apellido, historial_rutas):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas

    def a_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "historial_rutas": self.historial_rutas        
        }      
    
if __name__ == "__main__":
    lista = []
    data = DataJson('./datos/usuario.json')

    usuario1 = Usuario(
        1,
        "Bartolo",
        "Navarro",
        "Monumental, Panaderia del chuña, Fiama"
    )

    lista.append(usuario1.a_json())
    data.escribir_json(lista) 
    
