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
# Arquivo: exercicios3\capitulo 03\exercicio-03-09.py
##############################################################################

"""
Exercício 03-09: Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

Resposta:
"""
dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

converter_em_segundos = ((((dias * 24) * 60 ) * 60) +(horas * 60) * 60) + (minutos * 60) + segundos

print(converter_em_segundos)

