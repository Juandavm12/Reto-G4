"""
RETO TÉCNICO
========================================
"""

# ==========================================
# CÓDIGO PROBLEMÁTICO
# ==========================================

class SistemaBiblioteca:
    """
    ENCUENTRA LOS PROBLEMAS:
    1. ¿Cuántos objetos crea?
    2. ¿Cuántas responsabilidades tiene?
    3. ¿Quién DEBERÍA crear cada objeto?
    """
    
    def registrar_usuario(self, nombre, email):
        # Crea Usuario
        usuario = Usuario(nombre, email)
        
        # Crea Tarjeta (debería hacerlo Usuario)
        tarjeta = Tarjeta(usuario.id)
        
        # Guarda en BD (debería ser Repositorio)
        print(f"Guardando usuario y tarjeta en BD...")
        
        # Envía email (debería ser Notificador)
        print(f"Enviando email a {email}")
        
        return usuario
    
    def realizar_prestamo(self, usuario, libro):
        # Crea Prestamo
        prestamo = Prestamo(usuario.id, libro.id)
        
        # Actualiza libro directamente
        libro.disponible = False
        
        # Guarda en BD
        print(f"Guardando préstamo en BD...")
        
        # Notifica
        print(f"Notificando a {usuario.nombre}")
        
        return prestamo


class Usuario:
    def __init__(self, nombre, email):
        self.id = 1
        self.nombre = nombre
        self.email = email


class Tarjeta:
    def __init__(self, usuario_id):
        self.numero = "T-001"
        self.usuario_id = usuario_id


class Prestamo:
    def __init__(self, usuario_id, libro_id):
        self.id = 1
        self.usuario_id = usuario_id
        self.libro_id = libro_id


# Para el ejemplo (no cuenta como clase del diseño)
class Libro:
    def __init__(self, titulo):
        self.id = 1
        self.titulo = titulo
        self.disponible = True


# ==========================================
# PREGUNTAS PARA LA AUDIENCIA
# ==========================================

print("=" * 60)
print("RETO: Encuentra las violaciones (3 minutos)")
print("=" * 60)
print()
print("PREGUNTAS:")
print("1. ¿Cuántos objetos crea registrar_usuario()?")
print("2. ¿Quién DEBERÍA crear Tarjeta según Creator?")
print("3. ¿Cuántas responsabilidades tiene SistemaBiblioteca?")
print("4. ¿Qué code smell ves aquí?")
print()

# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":
    print("EJECUTANDO código problemático...")
    print("-" * 60)
    
    sistema = SistemaBiblioteca()
    usuario = sistema.registrar_usuario("Juan", "juan@email.com")
    libro = Libro("Clean Code")
    prestamo = sistema.realizar_prestamo(usuario, libro)
    
    print()
    print("Cuenta cuántos 'new' ves")
    print("Cuenta cuántas responsabilidades tiene SistemaBiblioteca")
