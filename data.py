import json
class DataJson:
    def __init__(self,ruta):
        self.ruta = ruta

    def escribir_json(self, lista):
        with open(self.ruta, 'w') as archivo:
            json.dump(lista, archivo, indent=4)

    def leer_json(self):
        try:
            with open(self.ruta, 'r') as archivo:
                datos_from_json = json.load(archivo)
            return datos_from_json
        except FileNotFoundError:
            return "No se encontró el archivo"
    
    
if __name__ == '__main__':    

    obj_json = DataJson('personas2.json')    
    personas = [
        {
            "nombre": "Luis",
            "apellido": "Perez"
        },
        {
            "nombre": "Lucas",
            "apellido": "Gonzales"
        }
    ]
    
    print(obj_json.leer_json())


