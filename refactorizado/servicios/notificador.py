class Notificador:
    """SRP: Responsabilidad única de envío de notificaciones."""

    def enviar_email(self, email):
        print(f"Enviando email a {email}")

    def notificar_usuario(self, usuario):
        print(f"Notificando a {usuario.nombre}")
