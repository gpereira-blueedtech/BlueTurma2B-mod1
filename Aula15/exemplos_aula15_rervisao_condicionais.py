# nome = input("Digite o nome: ")

# if, elif, else
"""
if nome == "Anderson":
    print("Você é o Anderson! Que bom")
    print("Nós gostamos muito do Anderson")
elif nome == "Ricardo":
    print("Você não é o Anderson! Você é o Ricardo!")
else:
    print("Você não é nenhum dos dois!")
print("Fico feliz que esteja aqui")
"""
# Diferença if, if e if, elif
"""
numero = int(input("Digite o número"))
if numero > 50: # se
    print("O número é maior que 50!")
elif numero > 30: # else if (senão, se) -> só testa se o if falhar. Depende da existência dele (if)
    print("O número é maior que 30")
elif numero > 10:
    print("O número é maior que 10")
else:
    print("O número é menor que 10")

print()

if numero > 50:
    print("O número é maior que 50!")
if numero > 30: # se -> testa independente do anterior ser verdade ou não.
    print("O número é maior que 30")
if numero > 10:
    print("O número é maior que 10")
else:
    print("O número é menor que 10")
"""

# if aninhado
"""
viaja = input("Você viaja de avião? [S / N] ")
if viaja == "S":
    opcao = input("Gostaria de ver prmoções?")
    if opcao == "S":
        print("Vá até uma de nossas agências!")
    else:
        print("Tá bom né, fazer o que...")
else:
    print("Ok, até a próxima!")
"""
