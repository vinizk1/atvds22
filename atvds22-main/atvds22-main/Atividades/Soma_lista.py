lista = []

while True:
    options = input (
        '''
            Escolha a opção:
            N: Novo numero;
            S: Soma;
            Q: Sair
        '''
    )

    if options == 'n':
        numero = int(input('Digite o numero'))
        lista.append(numero)

    elif options == 's':
        print(sum(lista))

    def sum(list):
        result = 0
        for i in list:
            result = result + 1
        return result