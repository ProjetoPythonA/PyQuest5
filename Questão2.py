listmatricul=[]
listsalbrut= []
listdescont= []
listsalliqui= []
x = 3
for c in range (x):
    listmatricul.append(int(input('Digite a matrícula: ')))
    listsalbrut.append(float(input('Digite o salário: ')))
    listdescont.append((listsalbrut[c] * 11) / 100)
    listsalliqui.append(listsalbrut[c] - listdescont[c])

print('      Matricula  Salario Bruto  Desconto  Salario Liquido')
for c in range (x):
    print(f'{listmatricul[c]:10} {listsalbrut[c]:15.2f} {listdescont[c]:15.2f} {listsalliqui[c]:15.2f}')
