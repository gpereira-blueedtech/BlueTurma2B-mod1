"""
a = int(input("digite 8: "))

while a != 8:
    print(f"{a} não é 8")
    a = int(input("digite 8: "))
print("Agora é 8!")
"""

"""
# Testando senha:
senha = "blue2021"
entrada = input("Digite a senha: ")

while entrada != senha:
    print("Senha incorreta!")
    entrada = input("Digite a senha: ")
print("Agora sim! Acesso liberado. Bem vindo à batcaverna!")
"""

# Criando uma lista de compras com número indefinido de itens
"""
lista = []
elemento = "elemento"
while elemento.upper() != "FIM":
    elemento = input("Digite o elemento, ou FIM para sair: ")
    if elemento.upper() != "FIM":
        lista.append(elemento)
        print("A lista está assim:")
        print(lista)
print("A lista está completa:")
print(lista)
"""

# Alternativa = lista.pop()
"""
lista = []
elemento = "elemento"
while elemento.upper() != "FIM":
    elemento = input("Digite o elemento, ou FIM para sair: ")
    lista.append(elemento)
    print("A lista está assim:")
    print(lista)
lista.pop() # Remove o último elemento da lista
print("A lista está completa:")
print(lista)
"""

# Alternativa:
"""
lista = []
elemento = "elemento"
while elemento.upper() != "FIM":
    elemento = input("Digite o elemento, ou FIM para sair: ")
    lista.append(elemento)
    print("A lista está assim:")
    print(lista)
print("A lista está completa:")
print(lista[:-1])
"""

# Uso do continue. Ele interrompe a execução atual do for e começa novamente
"""
lista = []
elemento = "elemento"
while elemento.upper() != "FIM":
    elemento = input("Digite o elemento, ou FIM para sair: ")
    if elemento.upper() == "CERVEJA":
        print("Cerveja não pode!")
        continue
    else:
        lista.append(elemento)
    print("A lista está assim:")
    print(lista)
print("A lista está completa:")
print(lista[:-1])
"""

# Exercício 0 – Crie um laço while que vai pedir para o usuário dois números 
# e faça a soma dos dois. 
# Enquanto a soma não for 50, ele deve continuar repetindo.
"""
entrada = int(input("Digite um número: "))
entrada2 = int(input("Digite um número: "))
while entrada + entrada2 != 50:
    print("A soma está incorreta! Não é 50")
    entrada = int(input("Digite um número novamente:"))
    entrada2 = int(input("Digite um número novamente:"))
print("A soma está correta! É 50")
"""