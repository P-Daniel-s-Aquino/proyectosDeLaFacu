import unittest
from tarjeta_baja import TarjetaBaja  # Importa la clase desde el archivo principal

class TestTarjetaBaja(unittest.TestCase):

    def setUp(self):
        """Este método se ejecuta antes de cada prueba individual."""
        self.tarjeta = TarjetaBaja(100)  # Inicializamos la tarjeta con saldo de 100

    def test_obtenerSaldo(self):
        """Prueba que el saldo inicial sea correcto."""
        saldo = self.tarjeta.obtenerSaldo()
        print(f"Saldo inicial: {saldo}")  # Imprime el saldo inicial
        self.assertEqual(saldo, 100)

    def test_cargarSaldo(self):
        """Prueba que cargar saldo aumente correctamente el saldo."""
        self.tarjeta.cargar(50)
        saldo_actual = self.tarjeta.obtenerSaldo()
        print(f"Saldo después de cargar 50: {saldo_actual}")  # Imprime el saldo actual
        self.assertEqual(saldo_actual, 150)

    def test_pagarViajeEnColectivo(self):
        """Prueba que pagar un viaje en colectivo descuente correctamente el saldo."""
        self.tarjeta.pagarViajeEnColectivo()
        saldo_actual = self.tarjeta.obtenerSaldo()
        viajes_colectivo = self.tarjeta.contarViajesEnColectivo()
        print(f"Saldo después de pagar colectivo: {saldo_actual}")  # Imprime el saldo
        print(f"Viajes en colectivo: {viajes_colectivo}")  # Imprime el número de viajes en colectivo
        self.assertEqual(saldo_actual, 100 - 21.5)
        self.assertEqual(viajes_colectivo, 1)

    def test_pagarViajeEnSubte(self):
        """Prueba que pagar un viaje en subte descuente correctamente el saldo."""
        self.tarjeta.pagarViajeEnSubte()
        saldo_actual = self.tarjeta.obtenerSaldo()
        viajes_subte = self.tarjeta.contarViajesEnSubte()
        print(f"Saldo después de pagar subte: {saldo_actual}")  # Imprime el saldo
        print(f"Viajes en subte: {viajes_subte}")  # Imprime el número de viajes en subte
        self.assertEqual(saldo_actual, 100 - 19.5)
        self.assertEqual(viajes_subte, 1)

    def test_saldoInsuficienteColectivo(self):
        """Prueba que no se pueda pagar un viaje en colectivo con saldo insuficiente."""
        tarjeta_pobre = TarjetaBaja(20)  # Tarjeta con saldo menor al costo de un viaje
        print(f"Saldo inicial (insuficiente): {tarjeta_pobre.obtenerSaldo()}")
        with self.assertRaises(ValueError):
            tarjeta_pobre.pagarViajeEnColectivo()

    def test_saldoInsuficienteSubte(self):
        """Prueba que no se pueda pagar un viaje en subte con saldo insuficiente."""
        tarjeta_pobre = TarjetaBaja(15)  # Tarjeta con saldo menor al costo de un viaje
        print(f"Saldo inicial (insuficiente): {tarjeta_pobre.obtenerSaldo()}")
        with self.assertRaises(ValueError):
            tarjeta_pobre.pagarViajeEnSubte()

    def test_contarViajes(self):
        """Prueba que el contador de viajes funcione correctamente."""
        self.tarjeta.pagarViajeEnColectivo()
        self.tarjeta.pagarViajeEnSubte()
        total_viajes = self.tarjeta.contarViajes()
        print(f"Total de viajes: {total_viajes}")  # Imprime el total de viajes
        print(f"Viajes en colectivo: {self.tarjeta.contarViajesEnColectivo()}")  # Imprime el número de viajes en colectivo
        print(f"Viajes en subte: {self.tarjeta.contarViajesEnSubte()}")  # Imprime el número de viajes en subte
        self.assertEqual(total_viajes, 2)
        self.assertEqual(self.tarjeta.contarViajesEnColectivo(), 1)
        self.assertEqual(self.tarjeta.contarViajesEnSubte(), 1)


if __name__ == '__main__':
    unittest.main()