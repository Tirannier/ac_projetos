"""
- AC 02:
- Aluno: Paulo Antonio Figueira
- Matrícula: 202401500704
- Curso: Ciência de Dados e Inteligência Artificial
- Professor: Victor Machado
- Disciplina: Programação Estruturada

"""
# Questão 02 da AC:
# Calculei direto, colocando o imposto de renda como uma constante, pois ele não varia, não o informando nos parâmetros. E sim, no cálculo diretamente.
def calculo_salario(valor_hora, num_horas):
    return round((valor_hora + num_horas) - (valor_hora + num_horas) * 0.275)
print(calculo_salario)

# Questão 01 da AC : a)

# eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0, supondo as raízes sempre reais;
#Usa as fórmulas, e retorna as raízes, tendo apresentasdo os valores reais em "a,b,c"
def eq_seg_grau(a = 1,b = 6,c=1):
    delta = ((-b)**2 - 4*a*c)
    x1 = (-b -delta**0.5) / (2*a)
    x2 = (-b +delta**0.5) / (2*a)



    return round(x1,x2)

# b)
#bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
# Lógica da função: ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0 
def anobissexto(ano):
    possibilidade_1 = 2000
    possibilidade_2 = 1900
    possibilidade_3 = 2010
    return int(ano = (possibilidade_1 == 0 and possibilidade_2 != 0 or possibilidade_3 == 0))
print(bool(anobissexto))



