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
# Arquivo: exercicios3\capitulo 03\exercicio-03-13.py
##############################################################################

"""Exercício 03-13: Escreva um programa que converta uma temperatura digitada em °C em °F

Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

     9 × C
 F = ----- + 32
       5

Resposta:
"""

temperatura_c = float(input("Digite a temperatura em ºC "))


temperatura_convertida = ((9 * temperatura_c) / 5) +32

print(f"A temperatura {temperatura_c}ºC convertida em F é {temperatura_convertida}ºF")

