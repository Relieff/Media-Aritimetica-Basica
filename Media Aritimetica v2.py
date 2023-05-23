from time import sleep
from math import trunc

resposta='S'
nota=final=0
listanum=[]

print('Olá Professor(a), a nota para o aluno ter média é 15.0 pontos. \n')
while resposta=='S':
    nota=listanum.append(float(input('Digite a nota do aluno: ')))   #Adicionei todo numero digitado em uma lista
    print('Deseja continuar \n[S] Sim [N] Não')
    resposta =str(input('---> ')).strip().upper()[0]
    
    if resposta=='N':
        break

final=sum(listanum)/2 #Somar os números da lista e dividir por 2.

if final >= 15:
    print('O aluno em questão está na média.')
else:
    print('O aluno em questão está de recuperação.')        
    

print(f'A nota final do aluno aplicando a média foi de: {final}')
