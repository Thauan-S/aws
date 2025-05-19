
import re
palavra = input("Insira uma palavra ou uma frase: ")
palavra_formatada = re.sub(r'[^a-zA-Z0-9]', '', palavra).lower()
palavra_invertida = palavra_formatada[::-1]
if palavra_formatada == palavra_invertida:
    print(f"A palavra/frase {palavra} é um palíndromo.")
else:
    print(f"A palavra/frase {palavra} não é um palíndromo.")