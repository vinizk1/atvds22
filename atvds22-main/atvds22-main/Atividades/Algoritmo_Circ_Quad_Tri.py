def circulo(raio):
    return 3.14159 * (raio ** 2)

def quadrado(lado):
    return lado ** 2

def triangulo(base, altura):
    return (base * altura) / 2

def escolher():
    print("1. Círculo")
    print("2. Quadrado")
    print("3. Triângulo")
    escolha = input("Escolha ai ")

    if escolha == "1":
        raio = float(input("funciona cu: "))
        print(f"area do círculo é {circulo(raio)}")
    elif escolha == "2":
        lado = float(input("quadrado: "))
        print(f"area do quadrado é {quadrado(lado)}")
    elif escolha == "3":
        base = float(input("triangulo: "))
        altura = float(input(" tamanho da altura do triângulo: "))
        print(f"A área do triângulo é {triangulo(base, altura)}")

escolher()