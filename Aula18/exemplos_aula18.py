class Aluno:
    def __init__(self,nome,classe,media):
        self.nome = nome
        self.classe = classe
        self.media = media
        self.escola = "Blue"

    # Criando os atributos fora do construtor (não uso self)
    # nome = "" 
    # classe = ""
    # media = 0

    def __str__(self):
        return f"O aluno {self.nome} da classe {self.classe} tem média {self.media}."

aluno = Aluno("Gustavo","3AM",7)
print(aluno.nome)
pedro = Aluno("Pedro","2AM",8)
print(pedro.nome)
print(pedro.classe)
print()
pedro.classe = "3AM"
print(pedro.nome)
print(pedro.classe)

# Criano um novo objeto através de input
"""
nome = input("Digite o nome do aluno: ")
classe = input("Digite a classe do aluno: ")
media = int(input("Digite a média do aluno: "))
aluno_novo = aluno(nome,classe,media)
print(vars(aluno_novo))
print(aluno_novo)
print()
del aluno_novo # Deletando o objeto
# print(aluno_novo) Erro - o objeto não existe mais
"""

# Criando um objeto vazio => não posso ter um construtor que obrigatoriamente peça parâmetros
"""
print(vars(everton))
print(type(everton))
print()
everton.nome = "Everton"
everton.classe = "3AM"
everton.media = 8
print(vars(everton))
everton.faltas = 8 #Criando um novo atributo
print(everton.faltas)
print(vars(everton))
"""