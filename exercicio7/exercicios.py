
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19,20]
for numero in numeros:
    if numero < 2:
        continue      
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False  
            break  
    if eh_primo:
        print(f"{numero} é primo.")
    else:
        continue

