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
# Arquivo: exercicios3\capitulo 03\exercicio-03-10.py
##############################################################################

"""
Exercício 03-10: Faça um programa que calcule o aumento de um salário

Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

Resposta:
"""

salario = float(input("Digite o valor do salário: "))

aumento = float(input(r"Digite quantos % de aumento: "))

aumento_salario = (salario * aumento) / 100

novo_salario = salario + aumento_salario

print(f"O aumento foi de {aumento_salario} e o novo salario é de {novo_salario}")