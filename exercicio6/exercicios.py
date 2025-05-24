def main():
    try:
        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: "))
        print(f"\nOlá, {nome}! Você tem {idade} anos.")
    except ValueError:
        print("\nIdade inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()