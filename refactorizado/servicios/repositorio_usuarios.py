class RepositorioUsuarios:
    """SRP: Responsabilidad única de persistencia de usuarios."""

    def guardar(self, usuario):
        print(f"Guardando usuario y tarjeta en BD...")
