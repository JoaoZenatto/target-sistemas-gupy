"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json

faturamento =''' {
   "faturamento": [18,2,3,4,5,0,0,8,9,10,11,12,0,0,15,16,17,18,19,0,0,22,23,24,25,26,0,0,29,5]
}'''

data = json.loads(faturamento)

   #remove os dias sem faturamento

valores = data['faturamento']
valores = [i for i in valores if i != 0]

   #menor = (min(valores)) pega o menor valor
   #maior = (max(valores)) pega o maior valor

   #Pega maior, menor e soma

menor = valores[0]
maior = valores[0]
sum = 0
for i in range(len(valores)):
   sum = sum + valores[i]
   if valores[i] > maior:
      maior = valores[i]
   if valores[i] < menor:
      menor = valores[i]

media = sum/len(valores)

   #dias maiores que a media
count = 0
for i in range(len(valores)):
   if (valores[i] > media):
      count += 1

maior = "{:.2f}".format(maior)
menor = "{:.2f}".format(menor)

print (f"Menor Faturamento do mês: R$:{menor}")
print (f"Maior Faturamento do mês: R$:{maior}")
print (f"Em {count} dias o faturamento foi maior que a media")

