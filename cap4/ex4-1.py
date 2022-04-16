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
# Arquivo: exercicios3\capitulo 04\exercicio-04-01.py
##############################################################################

"""
Exercício 04-01: O que acontece se o primeiro e o segundo valores forem iguais?

Analise o Programa 4.1. Responda o que acontece se o primeiro e o segundo valores forem iguais? Explique.

Resposta:
"""
#########
"""
pode acontecer diversos fatores, depende onde for utilizado
Ex:
se a = b
ocorrer uma condição a > b ou b > a vai retornar falso

Se os valores forem iguais, nada será impresso.
Isso acontece porque a > b e b > a são falsas quando a = b.
Assim, nem o print de 2, nem o print de 3 serão executados, logo nada será impresso.
"""