# Criando as funções: 
# "Ensinando" ao programa o que ele deve fazer quando a função for chamada
# Importante lembrar que nesse momento a função não é executada, apenas criada! 
# Para executar, eu preciso chamar a função pelo nome dela no programa 

def testa_idade(idade=18):
    print(idade)
    if idade >= 18:
       print("Maior de idade\n")
    else:
       print("Menor de idade\n")

def soma_tudo_do_sangue(hema, plaq, leuco):
    sangue_total = hema + plaq + leuco
    print("O sangue total é: ", sangue_total)
    return sangue_total


sangue = soma_tudo_do_sangue(10, 5, 30) #Armazena na var sangue o que foi retornado pela função chamada
#print("O sangue total é:", sangue)
#print(soma_tudo_do_sangue(8, 8, 8)) # Printa o retorno da função
#soma_tudo_do_sangue(7, 7, 7) # Apenas executa a função.


print("   SEMANA 1:\n")
sangue = soma_tudo_do_sangue(10, 5, 30)


if sangue > 300:
    print("Cuidado, você vai morrer\n\n")
else:
    print("Toma cuidado mesmo assim.\n\n")

print("   SEMANA 2:\n")
sangue = soma_tudo_do_sangue(180, 200, 2)


if sangue > 300:
    print("Cuidado, você vai morrer\n")
else:
    print("Toma cuidado mesmo assim.\n")

print("   SEMANA 3:\n")
h = int(input("Digite valor H: "))
p = int(input("Digite valor P: "))
l = int(input("Digite valor L: "))

sangue = soma_tudo_do_sangue(h, p, l)

if sangue > 300:
    print("Cuidado, você vai morrer\n")
else:
    print("Toma cuidado mesmo assim.\n")