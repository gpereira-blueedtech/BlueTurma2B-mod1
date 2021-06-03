class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,novo_salario):
        raise ValueError("Comando não permitido! Use o método calcular_salario()")

    def registra_hora_trabalhada(self,horas=1):
        self.__horas_trabalhadas += horas
        # self.horas_trabalhadas = self.horas_trabalhadas + horas

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

funcionario = Funcionario("Ycaro", "Analista de dados", 125)
# print(f"Salário atual: {funcionario.salario}")
# print(f"Horas trabalhadas: {funcionario.horas_trabalhadas}")
# print()
# horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
# funcionario.registra_hora_trabalhada(horas_trabalhadas)
# funcionario.calcula_salario()
# print(f"Salário atual: {funcionario.salario}")
# print(f"Horas trabalhadas: {funcionario.horas_trabalhadas}")
# print()
# funcionario.salario = 200
funcionario.registra_hora_trabalhada(10)
funcionario.calcula_salario()
funcionario.salario = 200
print(f"Salário atual: {funcionario.salario}")