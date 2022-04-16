##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2022
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 04\exercicio-04-09.py
##############################################################################

"""
Exercício 04-09: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa

Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário. 
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

Resposta:
"""

valor_casa = float(input("Digite o valor da casa: "))

salario = float(input("Digite o valor do seu salário: "))

anos_pagar = int(input("Quantos anos você vai pagar: "))

total_meses = anos_pagar * 12

valor_prestacao = valor_casa / total_meses

salario_30per = salario * 0.3

if valor_prestacao > salario_30per:
    print(f"Emprestimo não aprovado, pois 30% do salario é {salario_30per:.2f} e o valor da prestação é de {valor_prestacao:.2f}")
else:
    print(f"Emprestimo aprovado em {total_meses} com R${valor_prestacao:.2f}")