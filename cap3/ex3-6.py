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
# Arquivo: exercicios3\capitulo 03\exercicio-03-06.py
##############################################################################

"""
Exercício 03-06: Expressão para decidir se um aluno tem a média para passar de ano

Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
Para ser aprovado, todas as médias do aluno devem ser maiores que 7. 
Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

Resposta:
"""

materia1 = 8
materia2 = 5
materia3 = 7

media = (materia1 + materia2 + materia3) / 3



if media > 7:
    print(f"Aluno aprovado com nota {media:.2f}")
else:
    print(f"Aluno reprovado com nota {media:.2f}")