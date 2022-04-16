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
# Arquivo: exercicios3\capitulo 04\exercicio-04-03.py
##############################################################################

"""
Exercício 04-03: Escreva um programa que leia três números e que imprima o maior e o menor

Escreva um programa que leia três números e que imprima o maior e o menor.

Resposta:
"""

a = int(input("Digite 1 numero: "))
b = int(input("Digite 1 numero: "))
c = int(input("Digite 1 numero: "))

if a > b and a > c:
    print(f"O maior é {a}")
elif b > a and b > c:
    print(f"O maior é {b}")
else:
    print(f"O maior é {c}")
    
if a < b and a < c:
    print(f"O menor é {a}")
elif b < a and b < c:
    print(f"O menor é {b}")
else:
    print(f"O menor é {c}")
    
    