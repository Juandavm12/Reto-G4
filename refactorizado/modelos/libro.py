class Libro:
    def __init__(self, titulo):
        self.id = 1
        self.titulo = titulo
        self.disponible = True

    def marcar_no_disponible(self):
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True
