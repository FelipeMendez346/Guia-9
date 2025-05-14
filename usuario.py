from abc import abstractclassmethod
from abc import ABCMeta

class Usuario(metaclass=ABC):
    @abstractclassmethod
    def ver_resultados(self,molecula):
        pass