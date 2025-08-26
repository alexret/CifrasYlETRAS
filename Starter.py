import random
import sys
from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
)
import CheckWord

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

class VentanaLetras(QWidget):
    def __init__(self, letrasDisponibles):
        super().__init__()
        self.setWindowTitle("Validar palabra")
        self.letrasDisponibles = letrasDisponibles

        layout = QVBoxLayout()
        self.label = QLabel("Escribe la palabra:")
        self.textbox = QLineEdit()
        self.letrasLabel = QLabel(f"Letras disponibles: {', '.join(letrasDisponibles)}")
        self.botonValidar = QPushButton("Validar")
        self.botonValidar.clicked.connect(self.validarResultado)
        self.labelConfirmacion = QLabel("")
        self.labelConfirmacion.hide()

        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.letrasLabel)
        layout.addWidget(self.botonValidar)
        layout.addWidget(self.labelConfirmacion)
        self.setLayout(layout)

    def validarResultado(self):
        resultado = self.textbox.text().lower()
        if all(letra in self.letrasDisponibles for letra in resultado):
            if CheckWord.get_word_definition(resultado):
                self.labelConfirmacion.setStyleSheet("color: green")
                self.labelConfirmacion.setText("Palabra encontrada")
            else:
                self.labelConfirmacion.setStyleSheet("color: red")
                self.labelConfirmacion.setText("Palabra no encontrada")
        else:
            self.labelConfirmacion.setStyleSheet("color: red")
            self.labelConfirmacion.setText("Alguna letra no está en el listado")
        self.labelConfirmacion.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaInicial()
    ventana.show()
    sys.exit(app.exec())
