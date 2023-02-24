class Personaje:
    
    #definimos el constructor
    def __init__(self,esp,nom,alt):
    
        #atrivutos
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt

    #metodos
    
    def correr (self, status):
        if(status):
            print("el personaje " + self.__nombre + " esta corriendo")
        else:
            print("el personaje " + self.__nombre + " se detuvo")
    
    def lanzar_granadas(self):
        print("el personaje " + self.__nombre + " lanzo una granada")
        
    def recargarArma(self, municiones):
        cargador=10
        cargador=cargador + municiones
        print("el arma tiene " + str(cargador) + " balas")
      
    def __pensar(self):
        
        print("Estoy pensando ........")
      
        
    #gets y sets

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre= nom
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,es):
        self.__especie= es
        
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura= alt    
        