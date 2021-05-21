# REVISÃO FUNÇÃO
def calc(numA, numB, operador):
    print("O primeiro número é:",numA)
    print(f"O segundo número é: {numB}")
    if operador == "+":
        resultado = numA + numB
        print("O resultado é:", resultado)
    elif operador == "-":
        resultado = numA - numB
        print("O resultado é:", resultado)
    elif operador == "*":
        resultado = numA * numB
        print("O resultado é:", resultado)
    elif operador == "/":
        resultado = numA / numB
        print("O resultado é:", resultado)
    else:
        print("Operador não encontrado")


# VERSÃO ALTERNATIVA
def calc2(numA, numB, operador):
    print("O primeiro número é:",numA)
    print(f"O segundo número é: {numB}")
    if operador == "+":
        resultado = numA + numB
    elif operador == "-":
        resultado = numA - numB
    elif operador == "*":
        resultado = numA * numB
    elif operador == "/":
        resultado = numA / numB
    
    if operador not in "+-*/":
        print("Operador inválido")
    else:
        print("O resultado é:",resultado)
    return resultado

    #ALTERNATIVA 2
def calc3(numA, numB, operador):
    print("O primeiro número é:",numA)
    print(f"O segundo número é: {numB}")
    if operador in "+-*/":
        if operador == "+":
            resultado = numA + numB
        elif operador == "-":
            resultado = numA - numB
        elif operador == "*":
            resultado = numA * numB
        elif operador == "/":
            resultado = numA / numB
        print("O resultado é:",resultado)
    else:
        print("Operador inválido")
    return resultado
    
# ALTERNATIVA 3 - Não recomendado, sai do programa em caso de erro.
def calc(numA, numB, operador):
    print("O primeiro número é:",numA)
    print(f"O segundo número é: {numB}")
    if operador == "+":
        resultado = numA + numB
        print("O resultado é:", resultado)
    elif operador == "-":
        resultado = numA - numB
        print("O resultado é:", resultado)
    elif operador == "*":
        resultado = numA * numB
        print("O resultado é:", resultado)
    elif operador == "/":
        resultado = numA / numB
        print("O resultado é:", resultado)
    else:
        print("Operador não encontrado")
        exit()
"""
num1 = float(input("Entre o primeiro número: "))
num2 = float(input("Entre o segundo número: "))
op = input("Digite o operador: +, -, * ou / ")
quant_macas = calc2(num1,num2,op)

num3 = float(input("Entre o primeiro número: "))
num4 = float(input("Entre o segundo número: "))
op2 = input("Digite o operador: +, -, * ou / ")
quant_laranjas = calc3(num3,num4,op2)
"""


quant_frutas = calc2(num1,num2,op) + calc3(num3,num4,op2)
print(quant_frutas)
"""
print(quant_macas)
print(quant_laranjas)
compras = {"Maçã":quant_macas, "Laranjas":quant_laranjas, "Total":quant_frutas}
print(compras)
"""