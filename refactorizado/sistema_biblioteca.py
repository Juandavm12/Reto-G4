from .modelos.usuario import Usuario
from .modelos.prestamo import Prestamo
from .servicios.repositorio_usuarios import RepositorioUsuarios
from .servicios.repositorio_prestamos import RepositorioPrestamos
from .servicios.notificador import Notificador


class SistemaBiblioteca:
    """
    Refactorizado aplicando Creator (GRASP) y SRP (SOLID).
    Ahora solo orquesta las operaciones, delegando responsabilidades.
    """

    def __init__(self):
        self.repositorio_usuarios = RepositorioUsuarios()
        self.repositorio_prestamos = RepositorioPrestamos()
        self.notificador = Notificador()

    def registrar_usuario(self, nombre, email):
        # Creator: Usuario crea su propia Tarjeta internamente
        usuario = Usuario(nombre, email)

        # SRP: Repositorio se encarga de la persistencia
        self.repositorio_usuarios.guardar(usuario)

        # SRP: Notificador se encarga de las notificaciones
        self.notificador.enviar_email(email)

        return usuario

    def realizar_prestamo(self, usuario, libro):
        prestamo = Prestamo(usuario.id, libro.id)

        # SRP: Libro gestiona su propia disponibilidad
        libro.marcar_no_disponible()

        # SRP: Repositorio se encarga de la persistencia
        self.repositorio_prestamos.guardar(prestamo)

        # SRP: Notificador se encarga de las notificaciones
        self.notificador.notificar_usuario(usuario)

        return prestamo
