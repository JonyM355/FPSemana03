from collections import deque

while True:
    palavras = input("Digite palavras com um espaço de diferença\n> ").split()    

    queue = deque(palavras)

    print(queue)
    
    while queue:
        palavra = queue.popleft()

        if 'a' in palavra.lower():
            print(palavra)

    break