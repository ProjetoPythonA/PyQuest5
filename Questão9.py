A= []
B= []
C= []
for i in range(3):
    A.append(int(input('Digite um número para A: ')))
    B.append(int(input('Digite um número para B: ')))
    C.append(A[i] + B[i])
print(f'Tabela A - {A}')
print(f'Tabela B - {B}')
print(f'Tabela C - {C}')