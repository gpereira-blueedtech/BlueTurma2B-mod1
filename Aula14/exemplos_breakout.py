# Validação de senha (while)
"""
senha = "12345"
opc = 0
entrada = input("Digite a senha numérica: ")
while entrada != senha and opc < 3:
    print("A senha está incorreta!")
    entrada = input("Digite a senha numérica: ")
    if entrada == "654321":
        print("Essa senha não pode usar")
        continue # continue : Para a execução do laço e começa novamente
    opc += 1
    if opc == 3:
        print("Tentativas esgotadas")
        exit() # encerra o programa
if entrada == senha:
    print("A senha está correto! Bem vindo ao programa!")
print("Continuando o programa")
"""

nome = input("Digite o nome do jogador: ")
partidas = int(input("Digite a quantidade de partidas que ele jogou: "))

gols_por_partida = []

for jogo in range(partidas):
    gols_por_partida.append(int(input(f"Quantos gols foram feitos na partida {jogo+1}: "))) #SINTAXE: lista.append(valor) -> adiciona um novo valor à lista
total_gols = sum(gols_por_partida)
print("Nome:",nome)
print("Partidas:",partidas)
print("Lista de gols:",gols_por_partida)
print("Total de gols",total_gols)

dicionario = {"Nome": nome, "Partidas":partidas, "Gols_partida":gols_por_partida, "Total_gols":total_gols}

print(f'O jogador {dicionario["Nome"]} jogou {dicionario["Partidas"]}')
print(f'Fazendo: {dicionario["Gols_partida"]}, com um total de: {dicionario["Total_gols"]}')

for i,v in enumerate (dicionario["Gols_partida"]):
    print("No jogo",i+1,"ele fez",v,"gols")

#Fim do programa