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
# Arquivo: exercicios3\capitulo 04\exercicio-04-06.py
##############################################################################

"""
Exercício 04-06: Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

Resposta:
"""

distancia = int(input("Digite a distancia da viagem: "))

if distancia <= 200:
    valor = distancia + (distancia * 0.5)
else:
    valor = distancia + (distancia * 0.45)
    
print(f"O valor da passagem para distancia {distancia}km é de: {valor}")