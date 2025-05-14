class Acido_Nucleico(Molecula):
    def __init__(self):
        self.__nombre=None
        self.__tipo=None
        self.__secuencia=None
        self.__longitud=0
        self.__estructura_secundario=None
        self.__secuencia_codificante=False
    
    def simular(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_tipo(self):
        return self.__tipo

    def get_secuencia(self):
        return self.__secuencia
    
    def get_longitud(self):
        return self.__longitud
    
    def get_estructura_secundaria(self):
        return self.__estructura_secundario
    
    def get_secuencia_codificante(self):
        return self.__secuencia_codificante
        
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
    
    def set_tipo(self,newtipo):
        if isinstance(newtipo,str):
            if newtipo.upper()=="ARN" or newtipo.upper()=="ADN":
                self.__tipo=newtipo
    
    def set_secuencia(self,newsecuencia):
        if isinstance(newsecuencia,str):
            self.__secuencia=newsecuencia

    def set_longitud(self,newL):
        if isinstance(newL,int):
            self.__longitud= newL

    def set_estructura_secundaria(self,newestructurasec):
        if isinstance(newestructurasec,str):
            self.__estructura_secundario=newestructurasec
    
    def set_codificante(self,newcodificante):
        if isinstance(newcodificante,bool):
            self.__secuencia_codificante=newcodificante

    def obtener_info(self):
        print(f"Nombre: {self.__nombre}\n"
        f"Tipo: {self.__tipo}\n"
        f"Secuencia: {self.__secuencia}\n"
        f"Longitud: {self.__longitud}\n"
        f"Estructura secundaria: {self.__estructura_secundario}\n"
        f"Secuencia codificante: {self.__secuencia_codificante}\n")