while True:
    try:
        dimensao = float(input("Digite 2 para vetor 2D ou 3 para vetor 3D:"))
        if dimensao == 2 or dimensao == 3:
            break
        else:
            print ("Entrada inválida.")
    except ValueError:
        print ("Entrada inválida.")
if dimensao == 2:
    while True:
        try:
            x = float(input("Digite a coordenada x:"))
            break
        except ValueError:
            print ('Entrada inválida.')
    while True:
        try:
            y = float(input("Digite a coordenada y:"))
            break
        except ValueError:
            print ('Entrada inválida.')
    vetor = [x, y]
else:
    while True:
        try:
            x = float(input("Digite a coordenada x:"))
            break
        except ValueError:
            print ("Entrada inválida.")
    while True:
        try:
            y = float(input("Digite a coordenada y:"))
            break
        except ValueError:
            print ("Entrada inválida.")
    while True:
        try:
            z = float(input("Digite a coordenada z:"))
            break
        except ValueError:
            print ("Entrada inválida.")
    vetor = [x, y, z]
while True:
    try:
        escalar = float(input("Digite o escalar: "))
        break
    except ValueError:
        print ("Entrada inválida.")
if dimensao == 2:
    produto_x = x * escalar
    produto_y = y * escalar
    resultado = [produto_x, produto_y]
else:
    produto_x = x * escalar
    produto_y = y * escalar
    produto_z = z * escalar
    resultado = [produto_x, produto_y, produto_z]

print(f'A multiplicação do vetor {vetor} pelo escalar {escalar} resultou no vetor {resultado}.')
