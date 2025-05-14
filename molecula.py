from abc import abstractclassmethod
from abc import ABCMeta

class Molecula(metaclass=ABC):
    @abstractclassmethod
    def simular():
        pass
    @abstractclassmethod
    def obtener_info():
        pass