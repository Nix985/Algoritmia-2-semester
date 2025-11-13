from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, rojo=0, verde=0, azul=0, distancia=0.0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
        self.__distancia = distancia 
        distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)
    
    
    def __str__(self):
        return (
            f"Id: {self.__id}\n"
            f"Origen: ({self.__origen_x}, {self.__origen_y})\n"
            f"Destino: ({self.__destino_x}, {self.__destino_y})\n"
            f"Velocidad: {self.__velocidad}\n"
            f"Color: ({self.__rojo}, {self.__verde}, {self.__azul})\n"
            f"Distancia: {self.__distancia:.2f}\n"
        )
    
    def to_dict(self):
        return{
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "rojo": self.__rojo,
            "verde": self.__verde,
            "azul": self.__azul,
            "distancia": self.__distancia
        }
    



"""v01 = Particula (id=56, origen_x=23, origen_y=234, destino_x=765, destino_y=76, velocidad=543, rojo=5666, verde=333, azul=234)
print (v01)
"""