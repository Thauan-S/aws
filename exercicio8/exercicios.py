
nota = float(input("Avalie o restaurante (0 a 5 estrelas): "))

if nota == 5:
    print("★★★★★ - Excelente! Comida maravilhosa e ótimo atendimento!")    

elif nota >= 4:
    print("★★★★☆ - Muito bom! Voltaria com certeza.")    

elif nota >= 3:
    print("★★★☆☆ - Razoável, mas tem espaço para melhorar.")    

elif nota >= 2:
    print("★★☆☆☆ - Precisa melhorar em vários pontos.")    

elif nota >= 1:
    print("★☆☆☆☆ - Experiência ruim, não recomendo.")    

elif nota >= 0:
    print("☆☆☆☆☆ - Péssimo! Comida e serviço deixaram a desejar.")    

else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 5.")