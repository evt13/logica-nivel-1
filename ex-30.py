#Contar quantas vezes um número aparece em um vetor

numeros = [1,2,3,2,2,2]
contador = 0
for numero in numeros:
    if numero==2:
        contador=contador+1
print("o numero 2 se repetiu", contador)
