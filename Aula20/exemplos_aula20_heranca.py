class Pessoa:
    def __init__(self,nome,idade,cpf, telefone):
        self.__nome = nome # __atributo = Quando defino meu atributo com __ antes, 
                           # é convencionado que ele não deve ser acessível de fora da classe
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
        self.__contadorNome = 0

    # def __str__(self): # Retorna o que foi pedido quando chamar apenas o objeto (não um atributo ou método)
    #     return f"Nome: {self.__nome}, idade:{self.__idade}\nCPF: {self.__cpf}, Telefone: {self.__telefone}"
    
    # Método Get = Pegar, receber -> Defino o método que vai passar o valor do atributo para fora da classe
    def getNome(self): # Exemplo de Get com outra função além de retornar o valor
        self.__contadorNome += 1
        return self.__nome    

    def getIdade(self):
        return self.__idade

    def getCpf(self):
        return self.__cpf
    
    def getTelefone(self):
        return self.__telefone
    
    def getContadorNome(self):
        print(f"O nome {self.__nome} foi pesquisado {self.__contadorNome} vezes.")

    def saudacao(self):
        print("Seja bem-vindo!")


    # Método Set = Alterar -> Altera o valor de um atributo
    def setNome(self,nome):
        self.__nome = nome

    def setIdade(self,idade):
        self.__idade = idade
    
    def setCpf(self,cpf): # Exemplo de Set com outras funções além de alterar o valor
        senha = input("Informe a senha: ")
        if senha == "12345":
            self.__cpf = cpf
            print("CPF Alterado!")
        else:
            print("Senha incorreta!")
    
    def setTelefone(self, telefone):
        self.__telefone = telefone

        
class Advogado(Pessoa):
    def __init__(self, nome, idade, cpf, telefone, oab):
        self.__oab = oab
        super().__init__(nome, idade, cpf, telefone)

    def processar(self,cliente):
        print(f"Fique tranquilo, {cliente}, nós vamos tirar todo o dinheiro deles!!!")

    def saudacao(self):
        print("Seja bem-vindo ao meu magnífico escritório de advocacia!")


class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, telefone, crm):
        self.__crm = crm
        super().__init__(nome, idade, cpf, telefone)

    def examinar(self):
        print("Muito bem, acho que é uma virose...")
    
    def saudacao(self):
        print("Seja bem-vindo ao meu consultório! Você está bem?")

class Ortopedista(Medico):
    def __init__(self, nome, idade, cpf, telefone, crm):
        super().__init__(nome, idade, cpf, telefone, crm)
    
    def saudacao(self):
        print("Seja bem-vindo! O que você quebrou hoje?")



pessoa = Pessoa("João", 20, "054054054-54", "456465")

advogado = Advogado("Harvey", 30, "0888888-88", "123456", "oab 46464")
advogado2 = Advogado("Rafael", 20, "087087087", "456456", "oab464654")
medico = Medico("Francisco",20,"654654654","789456","crm 123456")
medico2 = Medico("Patch Adams", 45, "4654789", "54654", "crm 456456")

ortopedista = Ortopedista("Dr. Orto", 21, "asdfsdf", "sdfsdf", "orto asdasd")

pessoa.saudacao()
advogado.saudacao()
medico.saudacao()
ortopedista.saudacao()

# listaAdvogado = [advogado,advogado2]
# listaMedico = [medico,medico2]
# print(vars(advogado))

# for item in listaAdvogado:
#     print(item)
# for item in listaMedico:
#     print(item)

# advogado2.processar("Ycaro")
# medico.examinar()

# # Printando os atributos dos objetos dentro das listas sem usar o método __str__
# for item in listaAdvogado:
#     print(f"Nome: {item.getNome()}, Idade: {item.getIdade()}\nCPF: {item.getCpf()}, Telefone: {item.getTelefone()}", )
# for item in listaMedico:
#     print(f"Nome: {item.getNome()}, Idade: {item.getIdade()}\nCPF: {item.getCpf()}, Telefone: {item.getTelefone()}", )


# Testando atributos e métodos da superclasse
"""
print(vars(advogado))

advogado.setCpf("123123123123")
print(vars(advogado))
print(type(vars(advogado)))
"""

# Exemplos Get e Set
"""    
pessoa = Pessoa("Gabriel",18,"054054054-54","43 99989998")
pessoa2 = Pessoa("Nivia", 18, "021021021-21", "11 54445444")
print(pessoa.getNome())

pessoa.setNome("Eurico")
pessoa2.setNome("Mayara")
print(pessoa.getNome())
print(pessoa2.getNome())
print()

print(vars(pessoa2))
pessoa2.setCpf("000888999-70")
print(vars(pessoa2))
print()

pessoa.getContadorNome()
"""

#Exemplos de como usar o método Get
"""
print(pessoa.mostrarNome())

listaConvidados =[]
listaConvidados.append(pessoa.getNome())
print(listaConvidados)

nomecliente = pessoa.getNome()
print(nomecliente)
"""