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
# Arquivo: exercicios3\capitulo 03\exercicio-03-11.py
##############################################################################

"""
Exercício 03-11: Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto

Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

Resposta:
"""

mercadoria = float(input("Digite o preço da mercadoria: "))

desconto_perc = float(input("Digite o percentual do desconto: "))

valor_desconto = (mercadoria * desconto_perc) / 100

merc_com_desconto = mercadoria - valor_desconto


print(f"O valor do desconto é {valor_desconto} total a pagar é de {merc_com_desconto}")