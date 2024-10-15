class Nota:
    def __init__(self, valor_inicial):
        if 0 <= valor_inicial <= 10:
            self.valor = valor_inicial
        else:
            raise ValueError("El valor debe estar entre 0 y 10.")
    
    def obtenerValor(self):
        return self.valor
    
    def aprobado(self):
        match self.valor:
            case x if 0 <= self.valor <= 3:
                return "Nota de aplazo!"
            case x if 4 <= self.valor <= 6:
                return "Nota aprobatoria!"
            case x if 7 <= self.valor <= 10:
                return "Nota excelente!"
    
    def desaprobado(self):
        if 0 <= self.valor <= 3:
            return f"Recursa la materia, su nota es: {self.valor}"
        return "Nota suficiente para aprobar"
    
    def recuperar(self, nuevoValor):
        if 0 <= nuevoValor <= 10:
            if nuevoValor > self.valor:
                self.valor = nuevoValor
            else:
                return f"El nuevo valor ({nuevoValor}) no es superior al valor actual ({self.valor})."
        else:
            raise ValueError("El valor debe estar entre 0 y 10.")
