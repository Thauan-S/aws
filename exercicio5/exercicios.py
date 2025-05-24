def cadastrar_alunos():
    alunos = {}

    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break

        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i} para {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida. Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
        
        alunos[nome] = notas

    return alunos

def calcular_medias(alunos):
    medias = {}
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        medias[nome] = media
    return medias

def exibir_resultados(medias):
    print("\n--- Médias dos alunos ---")
    for nome, media in medias.items():
        print(f"{nome}: {media:.2f}")

    if medias:
        melhor_aluno = max(medias, key=medias.get)
        print(f"\nAluno com a maior média: {melhor_aluno} ({medias[melhor_aluno]:.2f})")
    else:
        print("\nNenhum aluno cadastrado.")

# Execução do programa
alunos = cadastrar_alunos()
medias = calcular_medias(alunos)
exibir_resultados(medias)
