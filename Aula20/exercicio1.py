class Ingresso:
    def __init__(self,valor):
        self.valorIngresso = valor
    
    def imprimirValor(self):
        print(self.valorIngresso)
        # return self.valorIngresso

class IngressoVIP(Ingresso):
    def __init__(self,valor,adicional):
        self.valorAdicional = adicional
        super().__init__(valor)
    
    def imprimirValorVIP(self):
        print(self.valorIngresso + self.valorAdicional)
        # return self.valorIngresso + self.valorAdicional

ingresso = Ingresso(10)
ingresso.imprimirValor()
ingressoVIP = IngressoVIP(10, 5)
ingressoVIP.imprimirValorVIP()

ingresso1 = ingresso.imprimirValor()
ingresso2 = ingressoVIP.imprimirValorVIP()
print("A diferença de valor é:",ingresso2 - ingresso1)

