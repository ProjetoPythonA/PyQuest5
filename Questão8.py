listanum= []
listpos = []
cont=maior= 0
for n in range(3):
    listanum.append(int(input('Digite um número: ')))
    if listanum[n] > maior:
        maior = listanum[n]
for n in range(3):
     if listanum[n] == maior:
        listpos.append(n)
        cont+=1
print(f'O maior valor digitado foi {maior} e aparece {cont} vezes nas posições', listpos)

