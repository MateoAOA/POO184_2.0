class Personaje:
    
    #atrivutos
    especie="Humano"
    nombre="cabo"
    altura:"2.70"

    #metodos
    
    def correr (self, status):
        if(status):
            print("el personaje" + self.nombre + "esta corriendo")
        else:
            print("el personaje" + self.nombre + "esta detuvo")
    
    def lanzar_granadas(self):
        print("el personaje" + self.nombre + "lanzo una granada")
        
    def recargarArma(self, municiones):
        cargador=10
        cargador=cargador + municiones
        print("el arma tiene " + cargador + " balas")
        