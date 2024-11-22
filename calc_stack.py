from collections import deque

stck1 = deque()

stck2 = deque()

num_separados = []

while True:
    numeros = input("Digite números com um espaço de diferença\n> ")    
    
    if numeros == "":
        print("Nenhum número foi selecionado")
        break

    else:
        numeros.split()
        for n in numeros:
            if n == " ":
                continue
            else:
                stck1.append(int(n))
        
        for num in stck1:
            resultado = num * 2
            stck2.append(resultado)
    
    print(stck1)

    stck2.reverse()
    for n in stck2:
        print(n)