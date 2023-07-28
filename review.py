from data import DataJson

class Review:
    def __init__(self, id, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def a_json(self):
        return {
            "id": self.id,
            "id_destino": self.id_destino,
            "id_usuario": self.id_usuario,
            "calificacion": self.calificacion,
            "comentario": self.comentario,
            "animo": self.animo

        }
        
if __name__ == "__main__":
    lista = []
    data = DataJson('./datos/review.json')   

    review1 = Review(
        1,
        1,
        1,
        5,
        "Excelente lugar",
        "Excelente"
    )

    lista.append(review1.a_json())
    data.escribir_json(lista)  
