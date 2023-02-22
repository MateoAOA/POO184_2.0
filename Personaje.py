class Personaje:
    
    #definimos el constructor
    def __init__(self,esp,nom,alt):
    
        #atrivutos
        self.especie= esp
        self.nombre= nom
        self.altura= alt

    #metodos
    
    def correr (self, status):
        if(status):
            print("el personaje " + self.nombre + " esta corriendo")
        else:
            print("el personaje " + self.nombre + " se detuvo")
    
    def lanzar_granadas(self):
        print("el personaje " + self.nombre + " lanzo una granada")
        
    def recargarArma(self, municiones):
        cargador=10
        cargador=cargador + municiones
        print("el arma tiene " + str(cargador) + " balas")
        
        