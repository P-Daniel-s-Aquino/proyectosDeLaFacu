""""""

class Persona:
    edad = 22
    nombre = "John Doe"
    pais = "Brasil"

doctor = Persona()
print("La edad es: ", doctor.edad)
#otra forma de msotrar el valor de un atributo
print("El nombre es: ", getattr(doctor, "nombre"))
#muestra si existe un atributo en el objeto.
print("El doctor tiene una edad?", hasattr(doctor, "edad"))
#muestra si existe un atributo en el objeto.
print("El doctor tiene un apellido?", hasattr(doctor, "apellido"))  
#cambia el valor del atributo.
setattr(doctor, "nombre", "Daniel")
#muestra el nuevo valor del atributo.
print(doctor.nombre)
#borra un atibuto en la clase
delattr(doctor, "pais")
#*ahora no existe por lo que muestra un error
# print(doctor.pais)