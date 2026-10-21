tupla_teste = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezasseis",
    "dezassete",
    "dezoito",
    "dezenove",
    "vinte",
)

Numero = int(input("Digite um numero entre 0 e 20: "))
if 0 <= Numero <= 20:
        print(f"Você digitou o numero {tupla_teste[Numero]}")
else:
        print("Número inválido. Digite um número entre 0 e 20.")

print(f"O seu numero por extenso é {tupla_teste[Numero]}")

