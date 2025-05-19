def par_ou_impar():
    pares = 0
    impares = 0

    print("Digite números inteiros. Quando quiser parar, digite 'fim'.\n")

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print("→ É par.\n")
                pares += 1
            else:
                print("→ É ímpar.\n")
                impares += 1
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número inteiro.\n")

    print("Programa encerrado.")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Executa a função
par_ou_impar()