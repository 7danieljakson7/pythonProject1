string = input("> ")

for i in string:
    if i.isupper():
        print(i, "- é minisculo")
    elif i.islower():
        print(i, "- é maisculo")
    elif i.isnumeric():
        print(f'caractere {i} é um numero')
    else:
        print(i, "- é numero ou outra coisa")