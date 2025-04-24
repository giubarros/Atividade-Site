import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


if a == 0:
    print("Não é equação do segundo grau")
else:

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não há raízes reais")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A raiz única é: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes são: {raiz1} e {raiz2}")
