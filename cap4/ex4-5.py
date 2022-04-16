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
# Arquivo: exercicios3\capitulo 04\exercicio-04-05.py
##############################################################################

"""
Exercício 04-05: Verifique se os resultados foram os mesmos do Programa 4.2 com else

Execute o Programa 4.4 e experimente alguns valores. Verifique se os resultados foram os mesmos do Programa 4.2.

Resposta: Sim foram os mesmos
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