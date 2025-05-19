
senha_correta = "12345678910"
tentativas = 0
while True:
    senha = input("Digite a senha: ")
    tentativas += 1
    if senha == senha_correta:
        print("Acesso permitido.")
        break
    else:
        print("Senha incorreta!")
    if tentativas == 3:
        print("Número de tentativas excedido, ACESSO NEGADO!")
        break