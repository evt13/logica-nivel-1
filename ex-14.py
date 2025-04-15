14) Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

print("digite um valor")
a=int(input())
if a>10:
  print("é maior que 10")
elif a<10:
     print("é menor que 10")
     #Se você quer testar se a é menor que 10, deve usar elif, que permite uma condição. O else é usado sem condição, apenas como "qualquer outro caso".
