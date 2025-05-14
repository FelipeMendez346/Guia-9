class Proteina(Molecula):
    def __init__(self):
        self.__nombre=None
        self.__peso_molecular=0.0
        self.__secuencia=None
        self.__estructura_3D=None
        self.__funcion=None
        self.__interactures=[]

    def simular(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_peso_molecular(self):
        return self.__peso_molecular

    def get__secuencia(self):
        return self.__secuencia

    def get_estructura_3D(self):
        return self.__estructura_3D
    
    def get_funcion(self):
        return self.__funcion

    def get_interactures(self):
        return self.__interactures

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
    
    def set_peso_molecular(self,newpeso):
        if isinstance(newpeso,float):
            self.__peso_molecular=newpeso
    
    def set_secuencia(self,newsecuencia):
        if isinstance(newsecuencia,str):
            self.__secuencia=newsecuencia
    
    def set_estrutura_3D(self,newestructura3D):
        if isinstance(newestructura3D,str):
            self.__estructura_3D=newestructura3D
    
    def set_funcion(self,newfuncion):
        if isinstance(newfuncion,str):
            self.__funcion=newfuncion
    
    def set_interactures(self,newlist):
        if isinstance(newlist,list):
            self.__interactures=newlist
    
    def agregar_metabolito(self,newmetabolito):
        if isinstance(newmetabolito,Metabolito):
            self.__interactures= self.__interactures + newmetabolito

    def obtener_info(self):
        print(f"Nombre: {self.__nombre}\n"
        f"Peso Molecular: {self.__peso_molecular}\n"
        f"Secuencia: {self.__secuencia}\n"
        f"Estrucutra 3D: {self.__estructura_3D}\n"
        f"Funcion: {self.__funcion}\n")
        f"interactures:\n"
        contador=1
        for Metabolito in self.__interactures:
                print(f"{contador}.{Metabolito.__nombre}")
                contador+=1

    