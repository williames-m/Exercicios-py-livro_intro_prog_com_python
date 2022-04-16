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
# Arquivo: exercicios3\capitulo 03\exercicio-03-14.py
##############################################################################

"""
Exercício 03-14: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

Resposta:
"""

dias_alugado = int(input("Quantos dias o carro foi alugado: "))

km_rodados = float(input("Quantos km você andou? "))

total_a_pagar = dias_alugado * 60 + km_rodados * 0.15

print(f"O total a pagar por {dias_alugado} dias e {km_rodados} km rodados é de: {total_a_pagar}")