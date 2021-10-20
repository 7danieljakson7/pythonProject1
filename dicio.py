telefones = {
    'daniel' : '123456789',
    'gii' : '987654321',
    'cassia': ' 882352'
}

print(telefones)

for nome in telefones:
    print(nome, telefones[nome])

print(telefones['daniel'])
print(telefones.get('diego'))
print(telefones.get('cassia'))

for (nome, telefone ) in telefones.items():
    print(telefone, 'é o numero do ', nome)
