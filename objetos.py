from Personaje import *

#crear objeto de la clase personaje

soldado = Personaje()

#usar atrivutos

print("Nombre: "+ soldado.nombre)
print("Especie: "+ soldado.especie)
print("Altura: "+ soldado.altura)

#usar metodos

soldado.correr(True)
soldado.lanzar_granadas()
soldado.recargarArma(87)
