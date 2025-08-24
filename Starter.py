import random

import CheckWord

cantidadVocales = int(input("cantidad de vocales: "))

cantidadLetras = []

consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                          'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vocales = ['a', 'e', 'i', 'o', 'u']

vocalesAsignadas = 0;


while len(cantidadLetras) != 10:

    cantidadLetras.append(random.choice(consonantes))

    if vocalesAsignadas != cantidadVocales:
        cantidadLetras.append(random.choice(vocales))
        vocalesAsignadas += 1

print(cantidadLetras)

resultado = input("Introduce la palabra que quieras ").lower().strip()

if all(letra in cantidadLetras for letra in resultado):
    CheckWord.get_word_definition(resultado)
else:
    print("Alguna letra no está")