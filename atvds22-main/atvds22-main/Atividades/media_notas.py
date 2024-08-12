notas = int(input("qtd de notas"))

soma = 0

for i in range(notas):
    nota = float(input("Digite a nota"))
    soma += nota

media = soma / notas

print(f"media das {notas} notas é {media}")
    