n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))

# o primeiro(1) numero é a base e o segundo(n2) é o expoente

resultado = 1

for i in range(n2):
    resultado *= n1

print("O resultado é:", resultado)
