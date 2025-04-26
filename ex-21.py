#21) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

# Leitura dos três valores
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Coloca os valores em uma lista e ordena
valores = [a, b, c]
valores.sort()

print(valores)
