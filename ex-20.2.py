20) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

# Leitura dos três valores
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Coloca os valores em uma lista e ordena
valores = [a, b, c]
valores.sort(reverse=True)

# Soma os dois maiores
soma = valores[0] + valores[1]

# Exibe o resultado
print("A soma dos dois maiores valores é:", soma)
