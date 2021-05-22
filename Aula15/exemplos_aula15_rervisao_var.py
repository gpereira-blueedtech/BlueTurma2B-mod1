var_str = "Blue"
var_int = 500
var_strnum = "500"
var_4 = " -=- "
var_list = [1,2,3,4,5]
# print(type(var_1))
# print(type(var_2))
# print(type(var_3))

print()
print(8 * var_4)
print("      Bem vindo ao meu programa!")
print(8 * var_4)
print()

# Transformando tipos de variáveis
"""
soma = var_2 + int(var_3)
var3_int = int(var_3)
print(type(var_3))
print(type(var3_int))
print(soma)
"""

# Testando se um valor está em uma string
"""
print("5" in var_str) #"Blue"
print("5" not in var_str)
print("B" and "e" in var_str) 
print("B" and "w" in var_str) 
# print("B" or "e" in var_str) # Não rola
print("B" and not "w" in var_str) 
print(not "B" and not "w" in var_str) 
print()
print("5" in var_strnum) #"500"
print(5 in range(var_int)) # 500
print(5 in var_list) #[1,2,3,4,5]

#Teste de or
num = 30
if num == 30 or num == 80:
    print("Deu certo!")
"""

# Maneiras de formatar uma string
"""
print ('%s comprou %d laranjas e comeu %.5f' % ('Mikael', 12, 0.5))
numero = float(input("Digite um número no formato x.xx: ").replace(",",".").replace("0","1"))
nome = input("Digite o nome: ")
lista = [10,20,30]
print(f"O usuário {nome} digitou: {numero:.2f}. A lista é {lista} Muito obrigado por usar!")
"""