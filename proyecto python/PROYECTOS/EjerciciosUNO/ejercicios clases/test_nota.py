import unittest
from nota import Nota

class TestNota(unittest.TestCase):
    
    def setUp(self):
        self.nueva_nota = Nota(10)
        
    def test_obtenerValor(self):
        self.assertEqual(self.nueva_nota.obtenerValor(), 10)
        print(f"La nota es un {self.nueva_nota.obtenerValor()}")

    def test_aprobado(self):
        self.assertEqual(self.nueva_nota.aprobado(), "Nota excelente!")
    
    def test_desaprobado(self):
        nota_baja = Nota(2)
        self.assertEqual(nota_baja.desaprobado(), "Recursa la materia, su nota es: 2")
    
    def test_recuperar(self):
        nota_baja = Nota(4)
        # Probamos un valor mayor
        nota_baja.recuperar(7)
        self.assertEqual(nota_baja.obtenerValor(), 7)  # El valor debe actualizarse a 7
        
        # Probamos un valor menor
        resultado = nota_baja.recuperar(5)
        self.assertEqual(nota_baja.obtenerValor(), 7)  # El valor no debe cambiar
        self.assertEqual(resultado, "El nuevo valor (5) no es superior al valor actual (7).")

if __name__ == "__main__":
    unittest.main()
