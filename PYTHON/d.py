a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

operacao = input("Escolha a operação (+, -, *, /): ")


if operacao == '+':
    resultado = a + b
    print(f"O resultado de {a} + {b} é: {resultado}")
elif operacao == '-':
    resultado = a - b
    print(f"O resultado de {a} - {b} é: {resultado}")
elif operacao == '*':
    resultado = a * b
    print(f"O resultado de {a} * {b} é: {resultado}")
elif operacao == '/':
    if b != 0:
        resultado = a / b
        print(f"O resultado de {a} / {b} é: {resultado}")
else:
    print("Erro!")
