"""
- AC 01:
- Aluno: Paulo Antonio Figueira
- Matrícula: 202401500704
- Curso: Ciência de Dados e Inteligência Artificial
- Professor: Victor Machado
- Disciplina: Programação Estruturada

"""

# Ano bissexto:
# Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos 
# (exceto anos múltiplos de 100 que não são múltiplos de 400).
# Expressão para saber se o ano é bissexto: ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0 
# Tem que ser divisivel por 4, e também, não pode ser divisivel por 100(nisto, achamos o módulo e colocamos !=0, por não poder ser divisível) ou então(or) o ano ser divisivel por 400(%400).

ano_bissexto = int (input("Informe o ano :"))
possibilidade_1 = ano_bissexto % 4 
possibilidade_2 = ano_bissexto % 100 
possibilidade_3 = ano_bissexto % 400 
print(possibilidade_1 == 0 and possibilidade_2 != 0 or possibilidade_3 == 0)

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












