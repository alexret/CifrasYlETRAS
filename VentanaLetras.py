from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

import CheckWord


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