from proteina import Proteina

class Metabolito(Proteina):
    def __init__(self):
        self.__nombre=None
        self.__formula_quimica=None
        self.__peso_molecular=0.0
        self.__via_molecular=None
        self.__polaridad=None
        self.__activo=False

    def simular(self):
        pass
    
    def get_nombre(self):
        return self.__nombre
    
    def get_formula_quimica(self):
        return self.__formula_quimica

    def get_peso_molecular(self):
        return self.__peso_molecular

    def get_via_molecular(self):
        return self.__via_molecular
    
    def get_polaridad(self):
        return self.__polaridad
    
    def get_activo(self):
        return self.__activo

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
    
    def set_formula_quimica(self,formula):
        if isinstance(formula,str):
            self.__formula_quimica=formula

    def set_peso_molecular(self,peso):
        if isinstance(peso,float):
            self.__peso_molecular=peso
    
    def set_via_molecular(self,Via):
        if isinstance(Via,str):
            self.__via_molecular
    
    def set_polaridad(self,Polaridad):
        if isinstance(Polaridad,str):
            if Polaridad.upper()=="POLAR" or Polaridad.upper()=="NO POLAR" or Polaridad.upper()=="ANFIPATICO":
                self.__polaridad=Polaridad
    
    def set_actividad(self,Activo):
        if isinstance(Activo,bool):
            self.__activo=Activo
        
    def obtener_info(self):
        print(f"Nombre: {self.__nombre}\n"
        f"Formula Quimica: {self.__formula_quimica}\n"
        f"Peso Molecular: {self.__peso_molecular}\n"
        f"Via Molecular: {self.__via_molecular}\n"
        f"Polaridad: {self.__polaridad}\n"
        f"Actividad: {self.__activo}\n")

a=Metabolito()
a.obtener_info()