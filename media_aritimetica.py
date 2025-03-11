from time import sleep

resposta='S'
nota=final=0
listanum=[]
bv= ('Olá Professor(a), seja bem vindo(a)! A nota que o aluno precisa para ter a média do bimestre é 15.0 pontos.')

print('='*200)
print(bv)
print('='*200 )
print('')


for nota in range(5):
    nota=listanum.append(float(input('Digite as 5 primeiras notas do aluno --> ')))   #Adicionei todo numero digitado em uma lista
    print('-'*30)
    while resposta=='S':
        resposta = str(input('Deseja continuar \n[S] Sim [N] Não'.strip().upper()[0])) 
    if resposta=='N':
        break

final=sum(listanum)/2 #Somando todos os numeros da lista e dividindo por 2 em seguida

print('Processando...')
sleep(0.5)
if final >= 15:
    print('O aluno em questão está na média.')
else:
    print('O aluno em questão está de recuperação.')        
    
sleep(0.3)
print(f'A nota final do aluno aplicando a média foi de: {final}')
