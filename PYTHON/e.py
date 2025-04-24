produto = input('Digite o nome do produto: ')
v_compra = float(input('Digite o valor de compra do produto: '))
if v_compra < 10.00:
    lucro = 0.70
elif 10 <= v_compra < 30:
    lucro = 0.50
elif 30 <= v_compra < 50:
    lucro = 0.40
else:
    lucro = 0.30

valor_venda = v_compra * (1 + lucro)

print(f"Produto: {produto}")
print(f"Valor de venda: R$ {valor_venda:.2f}")
