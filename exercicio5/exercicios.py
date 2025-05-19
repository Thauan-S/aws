
numero = int(input("Digite um número inteiro positivo: "))
if numero < 2:
    print(f"O número {numero} não é primo.")
else:
    e_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break
    if e_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")