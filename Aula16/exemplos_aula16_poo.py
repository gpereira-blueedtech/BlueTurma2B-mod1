class Herói():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def engordar(self, peso):
        self.peso += peso
    
    def salvar(self):
        print("O capitão salvou o mundo de novo. Nossa, que coisa...")

a = Herói("Capitão América",30,85)
b = Herói("Homem de Ferro",30,352)
print(vars(a))
print(vars(b))
a.salvar()
print()

a.engordar(10)
b.peso = 100
print(vars(a))
print(vars(b))

print()
b.peso = a.peso
print(f"O novo peso do {b.nome} é {b.peso}")

print("\n   === CLASSE PESSOA ===\n")
class Pessoa():
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def emagrecer(self, peso):
        self.peso -= peso
    

a = Pessoa('Steve Rogers',1.80, 90)
print(vars(a))
a.emagrecer(10)
print(vars(a))



            ### RETORNO 21:25 ###


