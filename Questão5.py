listnum = []
for n in range(3):
    listnum.append(int(input("Digite um número: ")))
listnum.sort()
print(f'Os números em ordem crescente ficam   {listnum}')
listnum.reverse()
print(f'Os números em ordem decrescente ficam {listnum}')