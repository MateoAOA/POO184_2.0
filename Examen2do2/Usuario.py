


class Usuario:
    
    #definimos el constructor
    def __init__(self,nom,ap,am,nac,car):
    
        #atrivutos
        self.__nombre= nom
        self.__apellidoP= ap
        self.__apellidoM= am
        self.__nacimiento= nac
        self.__carrera=car
        

    #metodos
    
    def generar (self):
        print(self.__nombre, self.__apellidoP, self.__apellidoM, self.__nacimiento, self.__carrera )
    
      
        
    #gets y sets

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre= nom
        
    def getEspecie(self):
        return self.__apellidoP
    
    def setEspecie(self,ap):
        self.__apellidoP= ap       
        
    def getAltura(self):
        return self.__apellidoM
    
    def setAltura(self, am):
        self.__apellidoM =am
    
    def getAltura(self):
        return self.__nacimiento
    
    def setAltura(self, nac):
        self.__nacimiento = nac
   
    def getAltura(self):
        return self.__carrera
    
    def setAltura(self, car):
        self.__carrera   =car  
   