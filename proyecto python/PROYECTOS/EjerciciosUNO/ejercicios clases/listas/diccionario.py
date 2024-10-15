class Diccionario:
    
    def __init__(self):
        self.palabras = {
            "coche" : "car",
            "perro" : "dog",
            "mesa" : "table",
            "gato" : "cat",
        }
    
    # Me permite agregar mas de dos argumentos al diccionario, 
    # mientras que la cantidad de argumentos sean dupletes      
    # def nuevos_pares(self, *args):
    # *args es una forma para que un metodo acepte una cantidad variable de argumentos posicionales
    #     if len(args) % 2 != 0: # Restringe a que los argumentos sena dupletes
    #         return f"Los argumentos deben estar de a apares"
    #     for a in range(0, len(args), 2):
    #         esp = args[a]     # Las palabras en español se guardan en la posicion de a
    #         ing = args[a+1]   # Las palabras en ingles se guardan en la siguiente posicion a respecto de a
    #         self.palabras.update({esp : ing}) # Se actualiza el diccionario
                                
    def nuevo_par(self, esp, ing):
        self.palabras.update({esp : ing})
        
    def traducir(self, palabra):
        for esp, ing in self.palabras.items():
            if palabra == esp:
                return ing
        else:
            return None
    
    def palabra_aleatoria(self):
        import random
        return random.choice(list(self.palabras.keys()))  
    
    def primera_letra_traduccion(self, palabra):
        traduccion = self.traducir(palabra)
        if traduccion:
            return f"La primera letra de {palabra} es {traduccion[0]}"
        else:
            return f"La palabra {palabra} no se encuentra en el diccionario"
    def cantidad_palabras(self):
        return len(self.palabras)
    
    def __str__(self):
        return str(self.palabras)
#---------------------------------------------------------------------------
diccionario = Diccionario()
    
print(diccionario)    

print(diccionario.traducir("mesa"))

print(diccionario.primera_letra_traduccion("mesa")) 

print(diccionario.primera_letra_traduccion("coco"))

print(diccionario.cantidad_palabras()) 

diccionario.nuevo_par("sol", "sun")

diccionario.nuevo_par("luna", "moon")

diccionario.nuevo_par("luna", "moon")

print(diccionario) 

#diccionario.nuevos_pares("sol", "sun", "luna", "moon")

print(diccionario.cantidad_palabras()) 

print(diccionario)