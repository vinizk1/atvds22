n = int(input("Digite o tamanho da lista"))

soma = 0

for i in range(n):
    nota = float(input("Digite a nota"))
    soma += nota

media = soma / n

print(f"media das {n} notas é {media}")
