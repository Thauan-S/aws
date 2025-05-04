
paises_capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Japão": "Tóquio",
    "Itália": "Roma",
    "Argentina":"Buenos Aires"
}

pais = input("Digite o nome de um país: ")

if pais in paises_capitais:
    print(f"A capital de {pais} é {paises_capitais[pais]}.")

