from Personaje import *
#solicitar datos

print("")
print("####### Datos Soldado #")
especieS= input("Escibir la especie del Soldado: ")
nombreS= input("Escibir el nombre del Soldado: ")
AlturaS= float(input("Escibir la altura del Soldado: "))
recargaS= int(input("Cuantas balas recargas al Soldado: "))

print("")
print("####### Datos Enemigo #")
especieE= input("Escibir la especie del Enemigo: ")
nombreE= input("Escibir el nombre del Enemigo: ")
AlturaE= float(input("Escibir la altura del Enemigo: "))
recargaE= int(input("Cuantas balas recargas al Enemigo: "))

#crear objeto de la clase personaje

soldado = Personaje(especieS,nombreS,AlturaS)
enemigo = Personaje(especieE,nombreE,AlturaE)

#usar atrivutos y metods
print("")
print("####### Objeto Soldado #")
print("Nombre: "+ soldado.nombre)
print("Especie: "+ soldado.especie)
print("Altura: "+ str(soldado.altura))

soldado.correr(True)
soldado.lanzar_granadas()
soldado.recargarArma(recargaS)

print("")
print("####### Datos Enemigo #")
print("Nombre: "+ enemigo.nombre)
print("Especie: "+ enemigo.especie)
print("Altura: "+ str(enemigo.altura))

enemigo.correr(False)
enemigo.lanzar_granadas()
enemigo.recargarArma(recargaE)
