"""
- AC 01:
- Aluno: Paulo Antonio Figueira
- Matrícula: 202401500704
- Curso: Ciência de Dados e Inteligência Artificial
- Professor: Victor Machado
- Disciplina: Programação Estruturada

"""

# Ano bissexto
# As minhas variáveis, descritas como: "possibilidade". Eu mesmo defini que fosse este termo, porque apresenta claramente que esta operação determinará que será bissexto, porque
# descobrindo a possibilidade, para o módulo == 0, acharemos que é verdadeiro, e sendo, =! 0 acharei falso. Daí, aplica-se a tabela verdadeira, com o print declarando o cálculo e expondo
# o que encontraremos no resultado.
ano_bissexto = int (input("Informe o ano :"))
possibilidade_1 = ano_bissexto % 4 == 0
possibilidade_2 = ano_bissexto % 100 == 100
possibilidade_3 = ano_bissexto % 400 == 0 
print(possibilidade_1 and not possibilidade_2) or (possibilidade_1 and possibilidade_3)

# Bhaskara: 
# ax^2 + bx + c
a = int(input("Digite o valor do coeficiente a "))
b = int(input("Digite o valor do coeficiente b "))
c = int(input("Digite o valor do coeficiente c "))
# Temos que achar o delta, primeiramente, com esses coeficientes informados no "input". Então, aplicamos a fórmula para determiná-lo.
delta = b**2 - 4*a*c  # Está representada, a fórmula: b^2 - 4ac
print("O valor de delta é: ", delta)
# Agora devemos calcular as raízes: delta > 0(duas raízes diferentes) ; delta = 0(duas raízes iguais) ; delta < 0(duas raízes complexas).
# x = (-b +- raiz(delta))/2a
x1 = (-b -delta**0.5) / (2*a)
x2 = (-b +delta**0.5) / (2*a)
print("O valor de x1 é: ", x1)
print("O valor de x2 é: ", x2)












