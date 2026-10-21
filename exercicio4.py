produtos = (
    ("Notebook", 3500.00),
    ("Mouse", 80.50),
    ("Teclado", 150.00),
    ("Monitor", 1200.00),
    ("Headset", 250.00),
    ("Cadeira Gamer", 1100.00),
    ("Mousepad", 45.00),
    ("Webcam", 220.00),
    ("Caixa de Som", 180.00),
    ("Pendrive", 35.00),
)


# Criando o cabeçalho da tabela
print("-" * 35)
print(f"{'PRODUTO':<20} | {'PREÇO':>10}")
print("-" * 35)

# a tupla e formatando em formato tabular
for produto, preco in produtos:
    print(f"{produto:<20} | R$ {preco:>7.2f}")

print("-" * 35)