import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Informe a quantidade de caracteres para a senha: "))
        if tamanho <= 0:
            print("O tamanho deve ser um número positivo.")
            return
        senha = gerar_senha(tamanho)
        print(f"Senha gerada: {senha}")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
