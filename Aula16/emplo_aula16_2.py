"""
class aluno():
    def __init__(self, nome_do_aluno,idade, serie, nota1, nota2, matricula, sala): # O nome do argumento não precisa ser o mesmo do atributo
        self.nome = nome_do_aluno
        self.escola = "Escola da Mayara"
        self.idade = idade
        self.serie = serie
        self.nota1 = nota1
        self.nota2 = nota2
        self.matricula = matricula
        self.sala = sala
        self.media = 0
    
    def calcula_media(self):
        self.media = (self.nota1+self.nota2)/2
        print(f"A média do {self.nome} é {self.media}")
    
    def altera_sala(self):
        nova_sala = input("Digite a nova sala")
        confirmacao = input(f"Você quer alterar o aluno {self.nome} da sala {self.sala} para a sala {nova_sala}?")
        if confirmacao == "S":
            self.sala = nova_sala
        else:
            print("Ok, nada alterado")
        print(f"A sala do(a) aluno(a) {self.nome} é: {self.sala}")

        

aluno_ycaro = aluno("Ycaro",18,"3AM",10,2,"087594","Sala 15")
aluna_nivia = aluno("Nívia",18,"3AM",9,5,"078524954","Sala 15")
# print(vars(aluno_ycaro))
# print(aluno_ycaro.nome)
print(vars(aluno_ycaro))
print(vars(aluna_nivia))
print()
aluno_ycaro.calcula_media()
aluna_nivia.calcula_media()
aluno_ycaro.altera_sala()
print(vars(aluno_ycaro))
print(vars(aluna_nivia))
"""

# Relembrando - definindo e chamando funções 
"""
def somar(num1,num2):
    total = num1+num2

somar(10,20)

batata = int(input("Digite: "))
n2 = int(input("Digite: "))

somar(batata,n2)
"""


# EXERCÍCIO 1:
"""
class pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def dados(self):
        print(f"O nome é: {self.nome} {self.sobrenome}, e a idade é {self.idade}")
        
gente = pessoa("Gabriel","Pereira",18)
print(vars(gente))
gente.dados()
"""

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def mostrar_dados(self):
        print(f"O nome é: {self.nome}, o sobrenome é: {self.sobrenome}, a idade é: {self.idade}")
        
nome = (input("Digite o nome: "))
sobrenome = (input("Digite o sobrenome: "))
idade = (input("Digite a idade: "))

a = Pessoa(nome, sobrenome, idade)
a.mostrar_dados()