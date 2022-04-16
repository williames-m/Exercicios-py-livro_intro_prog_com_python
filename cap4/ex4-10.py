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
# Arquivo: exercicios3\capitulo 04\exercicio-04-10.py
##############################################################################

"""
Exercício 04-10: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica

Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+

Resposta:
"""

kwh_consumida = int(input("Quanto é o kWh consumido: "))

tipo_instalacao = input("Qual é o tipo de instalação? R para residências, I para indústrias e C para comércios ").upper()

if tipo_instalacao == 'R':
    if kwh_consumida > 500:
        valor_pagar = kwh_consumida * 0.65
    else:
        valor_pagar = kwh_consumida * 0.40
        
elif tipo_instalacao == 'C':
    if kwh_consumida > 1000:
        valor_pagar = kwh_consumida * 0.60
    else:
        valor_pagar = kwh_consumida * 0.55
        
elif tipo_instalacao == 'I':
    if kwh_consumida > 5000:
        valor_pagar = kwh_consumida * 0.60
    else:
        valor_pagar = kwh_consumida * 0.55
else:
    print("Erro ! Tipo de instalação desconhecido!")
    
print(f"O valor a pagar é de {valor_pagar}")





