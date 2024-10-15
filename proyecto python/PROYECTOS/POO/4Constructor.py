"""__ asi comienzan los constructores que son metodos"""
class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    
    def descripcion(self):
        return "{} tiene {}".format(self.nombre, self.año)
    
    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)
    
doctor = Persona("Daniel", "25 años")
print(doctor.descripcion())
print(doctor.comentario("Hallöchen"))

#modificar un atributo

class EMail:
    def __init__(self):
        self.enviado = False
    
    def enviarCorreo(self):
        self.enviado = True
        
mi_correo = EMail()
print(mi_correo.enviado)

mi_correo.enviarCorreo()
print(mi_correo.enviado)
