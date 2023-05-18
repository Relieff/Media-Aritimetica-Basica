from time import sleep
from math import trunc

resposta = 'S'
nota = final = menor = maior = 0
listanum = []
menor = maior = 0

while resposta == 'S':
    nota = listanum.append(float(input('Digite a nota do aluno: ')))   #Adicionei todo numero digitado em uma lista
    print('Deseja continuar \n[S] Sim [N] Não')
    resposta =str(input('---> ')).strip().upper()[0]
    
    if resposta == 'N':
        break

    if final < 15:
        menor == final
    else:
        maior == final
        
final = sum(listanum)/2 #Somar os números da lista e dividir por 2.
  
print(f'A nota final do aluno aplicando a média foi de: {final}')
print(f'A menor nota foi {menor} e a maoir nota foi {maior}')
