"""clase persona"""

class Persona:
    doctor = "Victor"

class Jugadores:
    j1 = "Messi"
    j2 = "Ronaldo"

class Nombre:
    pass

"""esto sirve para crear objetos mas adelante en el codigo.
y se expresa con el nombre del objeto igualado a la clase con parametros vacios."""
victor = Nombre()
maria = Nombre()    

#objeto.atributo = valor    
victor.edad = 30
victor.sexo = "Masculino"
victor.pais = "Bolivia"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "Colombia"

print(Persona.doctor)

print(Jugadores.j2, Jugadores.j1)

print(victor.edad)
print(maria.edad)