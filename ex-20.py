#20) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

valor1= int(input("digite um valor "))
valor2= int(input("digite um valor "))
valor3= int(input("digite um valor "))
if valor3<valor1<valor2:
    print(valor1+valor2)
elif valor1<valor2<valor3:
    print(valor2+valor3)
elif valor1<valor3<valor2:
    print(valor3+valor2)
