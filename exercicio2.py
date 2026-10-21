tupla_times = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco da Gama",
    "Vitória",
    "Atlético-MG",
    "Fluminense",
    "Grêmio",
    "Juventude",
    "Red Bull Bragantino",
    "Athletico-PR", 
    "Criciúma",
    "Atlético",
    "Cuiabá",
)

# os 5 primeiros colocados 
for t in range(0, 4):
    print(f"os primeiros 5 colocados são {tupla_times[t]}")

# os ultimos 4 colocados 

for r in range(16, 20):
    print(f"os ultimos 4 colocadops são {tupla_times[r]}")

# time em ordem alfabetica
print(f"os times em ordem alfabetica são {sorted(tupla_times)}")

# em que posicao esta o time do flamengo
print(f"o time do flamengo esta na posicao {tupla_times.index('Flamengo') + 1} da tabela")