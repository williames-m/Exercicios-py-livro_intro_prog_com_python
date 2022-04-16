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
# Arquivo: exercicios3\capitulo 03\exercicio-03-12.py
##############################################################################

"""
Exercício 03-12: Escreva um programa que calcule o tempo de uma viagem de carro

Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

Resposta:
"""

distancia = float(input("Digite a distancia da viagem: "))

velocidade_media = float(input("Digite a velocidade média da viagem: "))

tempo_viagem = distancia / velocidade_media

print(f"O tempo de viagem é de {tempo_viagem} horas")