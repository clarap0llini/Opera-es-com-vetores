while True:
    dimensao = float(input("Digite 2 para vetor 2D ou 3 para vetor 3D:"))
    if dimensao == 2 or dimensao == 3:
        break
    else:
        print("Entrada inválida. Digite apenas 2 ou 3.")


if dimensao == 2:
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))
    vetor = [x, y]
else:
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))
    z = float(input("Digite a coordenada z: "))
    vetor = [x, y, z]

escalar = float(input("Digite o escalar: "))


if dimensao == 2:
    produto_x = x * escalar
    produto_y = y * escalar
    resultado = [produto_x, produto_y]
else:
    produto_x = x * escalar
    produto_y = y * escalar
    produto_z = z * escalar
    resultado = [produto_x, produto_y, produto_z]

print(f'A multiplicação do vetor {vetor} por escalar {escalar} resultou no vetor {resultado}')

