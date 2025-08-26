import random
import sys
from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
)

from entity.Player import Player
from forms.VentanaLetras import VentanaLetras

consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
               'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vocales = ['a', 'e', 'i', 'o', 'u']


class VentanaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cantidad de vocales")
        layout = QVBoxLayout()

        self.label = QLabel("Cantidad de vocales:")
        self.textboxVocales = QLineEdit()
        self.botonContinuar = QPushButton("Continuar")
        self.botonContinuar.clicked.connect(self.validarYContinuar)

        layout.addWidget(self.label)
        layout.addWidget(self.textboxVocales)
        layout.addWidget(self.botonContinuar)
        self.setLayout(layout)

    def validarYContinuar(self):
        texto = self.textboxVocales.text()
        if not texto.isdigit():
            QMessageBox.warning(self, "Error", "Introduce un número válido.")
            return

        cantidadVocales = int(texto)
        letrasGeneradas = self.generarLetras(cantidadVocales)
        self.hide()
        self.ventanaLetras = VentanaLetras(letrasGeneradas)
        self.ventanaLetras.show()

    def generarLetras(self, cantidadVocales):
        letras = []
        vocalesAsignadas = 0
        while len(letras) < 10:
            if vocalesAsignadas < cantidadVocales:
                letras.append(random.choice(vocales))
                vocalesAsignadas += 1
            else:
                letras.append(random.choice(consonantes))
        return letras


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaInicial()
    ventana.show()
    sys.exit(app.exec())
