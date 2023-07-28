from data import DataJson

class Ubicacion:
    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    def a_json(self):
        return {
            "id": self.id,
            "direccion": self.direccion,
            "coordenadas": self.coordenadas        
        }    
    
if __name__ == "__main__":
    lista = []
    data = DataJson('./datos/ubicacion.json')
 
    La_Fiamma = Ubicacion(
         1,
        "Catamarca 370",
        (-24.79470848769245, -65.4062539378253)
    )

    lista.append(La_Fiamma.a_json())
    data.escribir_json(lista) 