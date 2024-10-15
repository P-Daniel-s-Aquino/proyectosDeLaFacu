class TarjetaBaja:

    # post: saldo de la Tarjeta en saldoInicial.
    def __init__(self, saldoInicial):
        self.__saldo = saldoInicial
        self.__viajes_colectivos = 0
        self.__viajes_subtes = 0
        self.__costo_colectivo = 21.5
        self.__costo_subte = 19.5
    # post: devuelve el saldo actual de la Tarjeta
    def obtenerSaldo(self): 
        return self.__saldo

    # post: agrega el monto al saldo de la Tarjeta.
    def cargar(self, monto):
        self.__saldo += monto

    # pre : saldo suficiente.
    # post: utiliza 21.50 del saldo para un viaje en colectivo.
    def pagarViajeEnColectivo(self):
        if self.__saldo >= self.__costo_colectivo:
            self.__saldo -= self.__costo_colectivo
            self.__viajes_colectivos += 1
        else:
            raise ValueError("Saldo de la tarjeta insuficiente!")
             
    # pre : saldo suficiente.
    # post: utiliza 19.50 del saldo para un viaje en subte. 
    def pagarViajeEnSubte(self):
        if self.__saldo >= self.__costo_subte:
            self.__saldo -= self.__costo_subte
            self.__viajes_subtes += 1
        else:
            raise ValueError("Saldo de la tarjeta insuficiente!")
            
    # post: devuelve la cantidad de viajes realizados.
    def contarViajes(self):
        return self.__viajes_subtes + self.__viajes_colectivos

    # post: devuelve la cantidad de viajes en colectivo.
    def contarViajesEnColectivo(self):
        return self.__viajes_colectivos
    
    # post: devuelve la cantidad de viajes en subte.
    def contarViajesEnSubte(self):
        return self.__viajes_subtes

tb = TarjetaBaja(1000)
print(tb.obtenerSaldo()) 
tb.cargar(2000)
print(tb.obtenerSaldo())
tb.pagarViajeEnColectivo()
# tb.pagarViajeEnColectivo()
# tb.pagarViajeEnColectivo()
print(tb.contarViajesEnColectivo())
print(tb.obtenerSaldo())