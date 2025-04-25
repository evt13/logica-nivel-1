# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
etapas para resolver:
	1 - peça os 3 valores
	2 - descobrir e mostrar o maior

valor1= int(input("digite um valor "))
valor2= int(input("digite um valor "))
valor3= int(input("digite um valor "))
if valor2<valor1>valor3:
    print(valor1,"é o maior")
elif valor1<valor2>valor3:
    print(valor2,"é o maior")
elif valor1<valor3>valor2:
    print(valor3,"é o maior")


