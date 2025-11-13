from particula import Particula
import json

class AdministradorParticulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for v in self.__particulas:
            print (v)
    
    def __str__(self):
        return "".join(
            str(v) +  "\n" for  v in self.__particulas
        )
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w')as archivo:
                lista=[particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista,archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open (ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                if len(self.__particulas) == 0:
                    self.__particulas = [Particula(**particula) for particula in lista]
                else:
                    self.__particulas.extend([Particula(**particula) for particula in lista])

            return 1
        except:
            return 0


    """def abrir(self, ubicacion):
        print("Ubicación recibida:", repr(ubicacion))

        try:
            with open(ubicacion, 'r', encoding='utf-8') as archivo:
                lista = json.load(archivo)
                print("JSON cargado:", lista, type(lista))

                if len(self.__particulas) == 0:
                 self.__particulas = [Particula(**particula) for particula in lista]
                else:
                    self.__particulas.extend(
                        [Particula(**particula) for particula in lista]
                    )

            print("Partículas cargadas:", len(self.__particulas))
            return 1

        except Exception as e:
            print("ERROR al abrir:", type(e), e)
        return 0"""

