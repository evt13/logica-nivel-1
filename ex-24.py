# Pedir senha até que seja digitada a correta

print("Digite a senha para acessar o servidor:")
senha = int(input())  # A senha precisa ser lida aqui

while senha != 291116:
    print("Senha incorreta. Tente novamente:")
    senha = int(input())  # Tem que pedir a senha de novo dentro do loop

print("Acesso permitido!")
           
