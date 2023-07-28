from data import DataJson


class Actividad:
    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def a_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destino_id": self.destino_id,
            "hora_inicio": self.hora_inicio        
        }    
    
if __name__ == "__main__":
    lista = []
    data = DataJson('./datos/actividad.json')

    casona = Actividad(1, "Casona", "Caseros 2000", 21)

    lista.append(casona.a_json())
    data.escribir_json(lista)

