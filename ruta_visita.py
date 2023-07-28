from data import DataJson
class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def a_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destinos": self.destinos        
        }

if __name__ == "__main__":
    lista = []
    data = DataJson('./datos/ruta_visita.json')

    ruta_1 = RutaVisita(1, 'Salta centro', [1, 2, 3])
    ruta_2 = RutaVisita(2, 'Salta sur', [4, 5, 6])  
    lista.append(ruta_1.a_json())
    lista.append(ruta_2.a_json())
    data.escribir_json(lista)     