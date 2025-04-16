# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("Digite o número de maçãs compradas")
quantidade=int(input())
if quantidade >=12:
    preco_unitario = 1.00
elif quantidade <12:
    preco_unitario = 1.30
custo_total = quantidade * preco_unitario
print(f"O custo total da compra é R$ {custo_total:.2f}")


Esse é um recurso do Python chamado f-string (disponível a partir do Python 3.6), que permite inserir variáveis diretamente dentro de uma string de forma simples e legível.

A letra f antes das aspas indica que a string é formatada. Quando você usa f"algum texto {variável}", o conteúdo de variável é inserido diretamente dentro da string no local onde está a chave {}.

3. {custo_total:.2f}:
Dentro da f-string, temos uma expressão {custo_total:.2f}. Vamos detalhar:

custo_total: Esse é o nome da variável que contém o valor calculado do custo total da compra (quantidade de maçãs multiplicada pelo preço unitário).

: .2f: Isso é uma especificação de formatação que indica como o valor de custo_total deve ser exibido.

f: Significa formato de ponto flutuante (número com casas decimais).

.2: Define que queremos duas casas decimais.

Ou seja, :.2f diz ao Python para formatar o número custo_total para exibi-lo com exatamente duas casas decimais. Isso é muito útil quando lidamos com valores monetários, para garantir que os preços sejam exibidos corretamente (por exemplo, R$ 10,50 e não R$ 10,5).
