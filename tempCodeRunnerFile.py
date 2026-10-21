import random

numeros = tuple(random.randint(1, 100) for _ in range(5))

print (numeros)

#maior numero 

maior_numero = max(numeros)
print (f"o maior numero foi {maior_numero}")

#menor numero 
menor_numero = min(numeros)
print (f"o menor numero foi {menor_numero}")