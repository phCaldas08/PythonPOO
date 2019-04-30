class CartaoDeCredito:
    def __init__(self, limiteInicial):
        self.__limite = limiteInicial
        self.__limiteTotal = limiteInicial

    def Compra(self, valor):
        if(valor <= (self.__limite * 1.1) and self.__limite > 0):
            self.__limite -= valor

    def PagarConta(self, valor):
        if(self.__limite + valor > self.__limiteTotal):
            return False
        else:
            self.__limite += valor
            return true
