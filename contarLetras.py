import random

palabras = 'Si queremos hacer algo con los valores referidos por las claves, contamos con el mismísimo diccionario que recorremos para obtener dichos valores (para esto es que se hicieron los diccionarios).'

frecuenciaLetra = {}

for letra in palabras:
    if letra in frecuenciaLetra:
        frecuenciaLetra[letra] = frecuenciaLetra[letra] + 1
    else:
        frecuenciaLetra[letra] = 1

#print(frecuenciaLetra)

for clave in frecuenciaLetra:
    valor = frecuenciaLetra[clave]
    print(clave + ': ' + str(valor))
