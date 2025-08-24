import random
import sys

from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

import CheckWord

def validarResultado():
    resultado = textbox.text()
    if all(letra in cantidadLetras for letra in resultado):
        if(CheckWord.get_word_definition(resultado)):
            labelConfirmacion.setStyleSheet("color: green")
            labelConfirmacion.setText("Palabra encontrada")
            labelConfirmacion.show()
        else:
            labelConfirmacion.setStyleSheet("color: red")
            labelConfirmacion.setText("Palabra no encontrada")
            labelConfirmacion.show()
    else:
        print("Alguna letra no está")

app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Letras")

# Crear los widgets
label = QLabel("EEscribe la palabra")
textbox = QLineEdit()

# Crear el layout vertical y añadir los widgets
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(textbox)


cantidadVocales = int(input("cantidad de vocales: "))

cantidadLetras = []

consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                          'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vocales = ['a', 'e', 'i', 'o', 'u']

vocalesAsignadas = 0

while len(cantidadLetras) != 10:

    cantidadLetras.append(random.choice(consonantes))

    if vocalesAsignadas != cantidadVocales:
        cantidadLetras.append(random.choice(vocales))
        vocalesAsignadas += 1

# Crear los widgets         
letras = QLabel(f"Las letras son: {cantidadLetras}")

layout.addWidget(letras)
boton = QPushButton("Validar")
boton.clicked.connect(validarResultado)
layout.addWidget(boton)
labelConfirmacion = QLabel("")
labelConfirmacion.hide()
layout.addWidget(labelConfirmacion)
ventana.setLayout(layout)  
ventana.show()
# Ejecutar la aplicación


sys.exit(app.exec_())  