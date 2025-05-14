from proteina import Proteina
from acido_nucleico import Acido_Nucleico
from metabolito import Metabolito

class Investigador():
    def __init__():
        self.__nombre=None
        self.__Molecula_a_estudiar=None
        self.__tipo_molecula=None
    def set_nombre(self,nombre):
        pass              
    def get_nombre(self):
        return self.__nombre
    def set_proteina(self,proteina):
        if isinstance(proteina,Proteina):
            self.__Molecula_a_estudiar=Proteina
            self.__tipo_molecula="PROTEINA"
    def set_nucleotido(self,nucleotido):
        if isinstance(nucleotido,Acido_Nucleico):
            self.__Molecula_a_estudiar=nucleotido
            self.__tipo_molecula="ACIDO NUCLEICO"
    def set_metabolito(self,metabolito):
        if isinstance(metabolito,Metabolito):
            self.__Molecula_a_estudiar=metabolito
            self.__tipo_molecula="METABOLITO"
    def get_Molecula(self):
        return self.__Molecula_a_estudiar    
    def get_tipo(self):
        return self.__tipo_molecula


    def ver_resultados(self):
        if self.__tipo_molecula=="PROTEINA":
            print("El Investigador obtuvo los siguientes resultados de la molecula:\n")
            Proteina.obtener_info(self.__Molecula_a_estudiar)
        if self.__tipo_molecula=="ACIDO NUCLEICO":
            print("El Investigador obtuvo los siguientes resultados de la molecula:\n")
            Acido_Nucleico.obtener_info(self.__Molecula_a_estudiar)
        if self.__tipo_molecula=="METABOLITO":
            print("El Investigador obtuvo los siguientes resultados de la molecula:\n")
            Metabolito.obtener_info(self.__Molecula_a_estudiar)
        else:
            print("no se ha puesto una molecula a estudiar")
