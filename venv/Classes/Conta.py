from Classes.CartaoDeCredito import CartaoDeCredito

class Conta():
    def __init__(self):
        self.__saldo = 0
        self.__numConta = 123
        self.__acoes = []
        self.__cartaoDeCredito = 0

    def GetSaldo(self):
        return self.__saldo

    def GetNumConta(self):
        return self.__numConta

    def Saque(self, valor):
        if(valor >= self.__saldo):
            self.__acoes.append(True)
            self.__saldo -= valor
            return True
        else:
            self.__acoes.append(False)
            return False

    def Deposito(self, valor):
        self.__acoes.append(True)
        self.__saldo += valor

    def SolicitaCartaoDeCredito(self):
        if(self.__acoes.count(True) > self.__acoes.count(False) and self.__saldo > 100):
            self.__cartaoDeCredito = CartaoDeCredito()
            return True

    def GetCartaoDeCredito(self):
        if(self.__cartaoDeCredito == 0):
            return False
        else:
            return CartaoDeCredito