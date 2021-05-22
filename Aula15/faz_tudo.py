def principal(arg_a = 30, arg_b = 20):
    # num1 = float(input("Digite num1: "))
    # num2 = float(input("Digite num2: "))
    if arg_a > arg_b:
        print(f"O número {arg_a} é maior")
    elif arg_b > arg_a:
        print(f"O número {arg_b} é maior")
    else:
        print(f"O número {arg_a} e {arg_b} são iguais.")
    soma = arg_a + arg_b
    media = soma/2
    print("A soma é:",soma)
    return [media, soma]
   

def secundaria():
    print()
    print("Essa é secundaria")