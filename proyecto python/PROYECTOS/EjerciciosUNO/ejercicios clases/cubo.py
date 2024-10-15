class Cubo:

    ##
    # pre : longitud_lado es un valor mayor a 0.
    # post: inicializa el cubo a partir de la longitud de lado dada
    #
    def __init__(self, longitud_lado):
        if longitud_lado > 0:
            self.longitud = longitud_lado
        else:
            raise ValueError("La longitud del lado no puede ser 0 o negativa.")

    ##
    # post: devuelve la longitud de todos los lados del cubo
    #
    def obtenerLado(self):
        return self.longitud

    ##
    # pre : nuevo_lado es un valor mayor a 0.
    # post: cambia la longitud de todos los lados del cubo
    #
    def cambiarLado(self, nuevo_lado):
        if nuevo_lado > 0:
            if nuevo_lado != self.obtenerLado():
                self.longitud = nuevo_lado
        else:
            raise ValueError("La longitud del lado no puede ser 0 o negativa.")

    ##
    # post: devuelve el área de la superficie de una cara del cubo
    #
    def obtenerAreaCara(self):
        return self.longitud ** 2

    ##
    # post: devuelve el volumen del cubo
    #
    def obtenerVolumen(self):
        return self.longitud ** 3


# Ejemplo de uso:
cubo = Cubo(3)
print(cubo.obtenerLado())        # Devuelve 3
print(cubo.obtenerAreaCara())    # Devuelve 9 (3^2)
print(cubo.obtenerVolumen())     # Devuelve 27 (3^3)

cubo.cambiarLado(4)
print(cubo.obtenerLado())        # Devuelve 4
print(cubo.obtenerAreaCara())    # Devuelve 16 (4^2)
print(cubo.obtenerVolumen())     # Devuelve 64 (4^3)
