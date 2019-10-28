lista = []
quadrad = []
for n in range(4):
    lista.append(int(input('Digite um número: ')))
    quadrad.append(lista[n] * lista[n])
print(f'Os números digitados foram     {lista}')
print(f'Seus respectivos quadrados são {quadrad}')