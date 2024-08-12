lista = []
def soma_lista(lista):
    for i, enumerate in lista:
        ...

while True:
    options = input('n = novo número, s = soma, q = sair')

    if options == 'n':
        numero = int(input('número: '))
        lista.append(numero)
    elif options == 's':
        print(soma_lista(lista))
    elif options == 'q':
        break
print(lista)

