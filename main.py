while True:
    # Lê os valores de X e M
    X, M = map(int, input().split())
    
    # Condição de parada
    if X == 0 and M == 0:
        break
    
    # Cálculo da nova experiência
    E = M * X
    
    # Impressão do resultado
    print(E)
