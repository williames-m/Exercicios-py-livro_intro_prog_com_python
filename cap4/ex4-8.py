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
# Arquivo: exercicios3\capitulo 04\exercicio-04-08.py
##############################################################################

"""
Exercício 04-08: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar

Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). 
Exiba o resultado da operação solicitada.

Resposta:
"""

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

operacao = input("Qual operçaão deseja realizar? soma (+), subtração (-), multiplicação (*) e divisão (/) ")

if operacao == '+':
    print(a + b)
elif operacao == '-':
    print(a - b)
elif operacao == '*':
    print(a * b)
elif operacao == '/':
    print(a / b)
else:
    print("Operação inválida")