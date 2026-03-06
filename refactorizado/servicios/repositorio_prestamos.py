class RepositorioPrestamos:
    """SRP: Responsabilidad única de persistencia de préstamos."""

    def guardar(self, prestamo):
        print(f"Guardando préstamo en BD...")
