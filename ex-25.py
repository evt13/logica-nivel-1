#Somar números positivos digitados pelo usuário até que ele digite um número negativo

# Inicializa a variável soma com zero
soma = 0

# Início do loop
while True:
    # Solicita um número ao usuário
    numero = float(input("Digite um número ): "))

    # Se for negativo, mostra a soma atual e encerra
    if numero < 0:
        print(" Soma final:", soma)
        break #é usada para interromper a execução de um laço (loop) antes de que o ciclo seja concluído

    # Caso contrário, soma o número e mostra a soma atual
    soma += numero
    print("Soma atual:", soma)
