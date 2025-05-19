def calculadora():
    while True:
        try:
            # Solicita os números ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Solicita a operação desejada
            operacao = input("Digite a operação (+, -, *, /): ")

            # Verifica se a operação é válida
            if operacao not in ['+', '-', '*', '/']:
                raise ValueError("Operação inválida. Use apenas +, -, * ou /.")

            # Realiza a operação
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2

            # Exibe o resultado
            print(f"Resultado: {resultado}")
            break  # Sai do loop após operação bem-sucedida

        except ValueError as ve:
            # Trata entrada inválida ou operação desconhecida
            print(f"Erro de entrada: {ve}. Tente novamente.")
        except ZeroDivisionError as zde:
            print(f"Erro matemático: {zde}. Tente novamente.")
        except Exception as e:
            # Trata qualquer outro erro genérico
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

# Executa a calculadora
if __name__ == "__main__":
    calculadora()