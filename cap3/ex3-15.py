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
# Arquivo: exercicios3\capitulo 03\exercicio-03-15.py
##############################################################################

"""
Exercício 03-15: Escreva um programa para calcular a redução do tempo de vida de um fumante

Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. 
Exiba o total em dias.

Resposta:
"""

cigarro_dias = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você fuma? "))

min_perdidos = cigarro_dias * 10

total_dias_perdidos = (anos_fumando * 365) + ((min_perdidos / 60) / 24)

print(f"total de dias perdidos é: {total_dias_perdidos:.2f}")
