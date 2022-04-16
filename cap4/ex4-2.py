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
# Arquivo: exercicios3\capitulo 04\exercicio-04-02.py
##############################################################################

"""
Exercício 04-02: Escreva um programa que pergunte a velocidade do carro de um usuário e diga se este foi ou não multado

Escreva um programa que pergunte a velocidade do carro de um usuário. 
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

Resposta:
"""

velocidade = int(input("Digite a velocidade do carro: "))

velocidade_max = 80

if velocidade > velocidade_max:
    valor = 0
    for _ in range(velocidade - velocidade_max):
        valor += 5
    print(f"Foi multado em R${valor}")
    
else:
    print("Não foi multado")