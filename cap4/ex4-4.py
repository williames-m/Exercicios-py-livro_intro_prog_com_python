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
# Arquivo: exercicios3\capitulo 04\exercicio-04-04.py
##############################################################################

"""
Exercício 04-04: Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

Resposta:
"""

salario = float(input("Digite o valor do salário: "))

if salario > 1250:
    salario_aumento = salario + (salario * 0.1)
else:
    salario_aumento = salario + (salario * 0.15)
    
print(f"O valor do salario será de {salario_aumento:.2f}")