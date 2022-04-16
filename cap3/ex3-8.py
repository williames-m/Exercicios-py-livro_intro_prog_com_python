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
# Arquivo: exercicios3\capitulo 03\exercicio-03-08.py
##############################################################################

"""
Exercício 03-08: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

Resposta:
"""

metros = int(input("Digite o tamanho em metros: "))

converter_mm = metros * 1000

print(f"Valor {metros}m em milímetros é: {converter_mm}mm")