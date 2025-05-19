import random  # Importa o módulo random para gerar números aleatórios

numero_secreto = random.randint(1, 10)

tentativas = 0

print("Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

while True:

    palpite = int(input("Digite seu palpite: "))
    
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        break  
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")