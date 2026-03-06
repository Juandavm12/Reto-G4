from refactorizado.sistema_biblioteca import SistemaBiblioteca
from refactorizado.modelos.libro import Libro


if __name__ == "__main__":
    print("EJECUTANDO código refactorizado...")
    print("-" * 60)

    sistema = SistemaBiblioteca()
    usuario = sistema.registrar_usuario("Juan", "juan@email.com")
    libro = Libro("Clean Code")
    prestamo = sistema.realizar_prestamo(usuario, libro)

    print()
    print("Ahora cada clase tiene UNA sola responsabilidad (SRP)")
    print("Y cada objeto es creado por quien lo contiene (Creator)")
