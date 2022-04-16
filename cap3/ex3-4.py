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
# Arquivo: exercicios3\capitulo 03\exercicio-03-04.py
##############################################################################

"""
Exercício 03-04: Crie uma expressão para determinar se uma pessoa deve ou não pagar imposto

Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

Resposta:
"""

salario = 1199.00

if salario > 1200:
    print("Paga imposto")
else:
    print("Não paga imposto")