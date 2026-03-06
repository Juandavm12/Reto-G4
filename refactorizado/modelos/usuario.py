from .tarjeta import Tarjeta


class Usuario:
    """Creator (GRASP): Usuario crea Tarjeta porque la contiene/agrega."""

    def __init__(self, nombre, email):
        self.id = 1
        self.nombre = nombre
        self.email = email
        self.tarjeta = self._crear_tarjeta()

    def _crear_tarjeta(self):
        return Tarjeta(self.id)
