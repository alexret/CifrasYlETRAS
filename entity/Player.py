class Player():
    def __init__(self, nombre):
        self.nombre = nombre

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, nuevo_nombre):
            if not isinstance(nuevo_nombre, str):
                raise ValueError("El nombre debe ser una cadena")
            self._nombre = nuevo_nombre

        @property
        def puntuacion(self):
            return self._puntuacion
        @puntuacion.setter
        def puntuacion(self, puntuacion):
            if not isinstance(puntuacion, float):
                raise ValueError("El puntuacion debe ser una cadena")
            self._puntuacion = puntuacion