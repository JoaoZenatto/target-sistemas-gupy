"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""

import json
from re import sub
from decimal import Decimal


with open('json_q4.json') as f:
    data = json.load(f)

    #converte para int e pega a soma total
UF = []
valores = []
sum = 0
for estado in data['estados']:
    faturamentoint = estado['faturamento'].replace("."," ")
    faturamentoint = faturamentoint.replace(",",".")
    faturamentoint = faturamentoint.replace(" ",",")
    faturamentoint = Decimal(sub(r'[^\d.]', '', faturamentoint))
    valores.append(faturamentoint)
    UF.append(estado['sigla'])
    sum += faturamentoint

    #calcula porcentagem
for i in range (len(data['estados'])):
    percentage = 100 * float(valores[i])/float(sum)
    percentage = "{:.2f}".format(percentage)
    print (f"{UF[i]} = {percentage}%")