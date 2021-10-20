nomes = [
    'daniel',
    'gii',
    'juan',
    'bispo',
    'cassia',
    'matheus'
]

nomes_copia = nomes.copy()
nomes_copia = nomes.clear()

print('nomes_copia:', nomes_copia)
print('index of gii', nomes.index('gii'))
nomes.insert(3, 'daniel')
print('pos insert ',nomes)
print('pos popada ',nomes.pop)
print('pos pop', nomes)
print('lista popada (index 2 ): ',nomes.pop(2))
print('pos pop index 2', nomes)
nomes.remove('juan')
print('pos reverse,nome', nomes)
nomes.reverse()
print('pos reverse',nomes)
nomes.sort()
print('pos sort', nomes)
nomes.sort(reverse=True)
print('pos sort reversed', nomes)

print('sobreviventes:')
for nome in nomes:
    print(nome)