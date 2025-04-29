#Somar números positivos digitados pelo usuário até que ele digite um número negativo

# Inicializa a variável soma com zero
soma = 0

# Início do loop
while True:
    # Solicita um número ao usuário
    numero = float(input("Digite um número positivo (ou negativo para parar): "))

    # Se for negativo, mostra a soma atual e encerra
    if numero < 0:
        print("Número negativo digitado. Soma final:", soma)
        break

    # Caso contrário, soma o número e mostra a soma atual
    soma += numero
    print("Soma atual:", soma)
