from data import DataJson

class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def a_json(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "tipo_cocina":self.tipo_cocina ,
            "ingredientes":self.ingredientes,
            "precio_minimo":self.precio_minimo,
            "precio_maximo":self.precio_maximo,
            "popularidad":self.popularidad,
            "disponibilidad":self.disponibilidad,
            "ubicacion":self.id_ubicacion,
            "imagen":self.imagen
        }    

if __name__ == "__main__":
    lista = []
    data = DataJson('./datos/destino_culinario.json')
    mamma_mia = DestinoCulinario(
        1,
        "Mamma Mia",
        "Italiana",
        ["harina", "tomate", "carnes", "huevos"],
        1800,
        5000,
        4.2,
        True,
        1,
        "imagen1"

    )
    lista.append(mamma_mia.a_json())
    data.escribir_json(lista)

