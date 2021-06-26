import itertools

string = input("Digite a string a ser permutada: ")

resultado = itertools.permutations(string, len(stringp))

for i in resultado:
    print(''.join(i))

