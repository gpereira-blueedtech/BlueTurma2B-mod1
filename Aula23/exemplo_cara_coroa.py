import random # Biblioteca usada para gerar resultados aleatórios

class Lancador:
    def __init__(self):
        self.moeda = "Cara"
        self.dado = 1
  
    def lanca_dado(self):
        self.dado = random.randint(1,6) # randint gera um valor inteiro aleatório entre os valores dos argumentos passados
        # print(f"Você rolou: {self.dado}") # printa o resultado e não retorna para quem chamou
        return self.dado # Retorna o valor informado quando for chamado
    
    def lanca_moeda(self):
        self.moeda = random.randint(1,2)
        if self.moeda == 1:
            print("Deu cara!")
        else:
            print("Deu coroa!")


objLancador = Lancador() # Criei o objeto (instanciei)

# Chamei o método (executei o que foi definido na classe)
# objLancador.lanca_dado() # Usado se o método já incluir o print. 
                         # Não vai retornar nem armazenar o valor, só printar
objLancador.lanca_moeda()

resultado = objLancador.lanca_dado() #Usado com o return. Vai armazenar o que foi retornado
print(f"Você rolou um: {resultado}")

# print("Você rolou um", objLancador.lanca_dado())  # Usado com return, printando direto o que foi retornado sem armazenar


# Exemplo de criação de classe e objeto

"""
class Carro:
    def __init__(self,modelo,ano,cor): 
        self.modelo = "Gol"
        self.ano = "2021"
        self.cor = "Branco"
    
    # def __init__(self):
    #     pass
    
    def dirigir():
        pass

    def acelerar():
        pass
        
Carro.dirigir() # A classe não executa métodos!! Ela é a "fábrica", diz como serão os objetos.
                # Se eu quiser usar os métodos e atributos, tenho que criar um objeto dessa classe:

# Sempre que for instanciar um objeto eu tenho que seguir a quantidade de argumentos que o meu
# Construtor pediu na classe. 

# nome_do_objeto = Classe(argumentos(podem ou não ser obrigatórios)) # Sintaxe

meu_carro = Carro("Gol","2021","Preto") # Construção do objeto caso o construtor peça argumentos
meu_carro.dirigir() # O objeto criado pode executar o método definido pela classe. 

# meu_carro = Carro() # Construção do objeto caso o construtor não peça nenhum argumento
"""
