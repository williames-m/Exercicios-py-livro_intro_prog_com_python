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
# Arquivo: exercicios3\capitulo 03\exercicio-03-02.py
##############################################################################

"""
Exercício 03-02: Complete a tabela com o resultado da expressão booleana correspondente

Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

Expressão Resultado        Expressão Resultado
a == c    ○ True ○ False   b > a     ○ True ○ False
a < b     ○ True ○ False   c >= f    ○ True ○ False
d > b     ○ True ○ False   f >= c    ○ True ○ False
c != f    ○ True ○ False   c <= c    ○ True ○ False
a == b    ○ True ○ False   c <= f    ○ True ○ False
c < d     ○ True ○ False

Resposta:
"""
print("a == c -> False")
print("a < b -> True")
print("d > b -> False")
print("c != f -> False")
print("a == b -> False")
print("c < d -> False")
print("b > a -> True")
print("c >= f -> True")
print("f >= c -> True")
print("c <= c -> True")
print("c <= f -> True")