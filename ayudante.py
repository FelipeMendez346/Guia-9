class Ayudante(Investigador):
    def __init__():
        self.__nombre=None
        self.__Molecula_a_estudiar=[]
    def set_nombre(self,nombre):
        pass              
    def get_nombre(self):
        return self.__nombre
    def set_proteina(self,proteina):
        if isinstance(proteina,Proteina):
            self.__Moleculas_a_estudiar=self.__Moleculas_a_estudiar+proteina
    def set_nucleotido(self,nucleotido):
        if isinstance(nucleotido,Acido_Nucleico):
            self.__Moleculas_a_estudiar==self.__Moleculas_a_estudiar+nucleotido
    def set_metabolito(self,metabolito):
        if isinstance(metabolito,Metabolito):
            self.__Moleculas_a_estudiar=self.__Moleculas_a_estudiar+metabolito
    def get_Molecula():
        return __Molecula_a_estudiar    
    def get_tipo():
        return __tipo_molecula
    def ver_resultados_proteina(self,n):
        print("El ayudante obtuvo los siguientes resultados de la proteina:\n")
        Proteina.obtener_info(self,n)
    def ver_resultados_Acido_nucleico(n):    
        print("El ayudante obtuvo los siguientes resultados del acido nucleico:\n")
        Acido_Nucleico.obtener_info(n)
    def ver_resultados_Metabolito(self,n):
        print("El ayudante obtuvo los siguientes resultados de el metabolito:\n")
        Metabolito.obtener_info(n)


