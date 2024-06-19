def encontrar_algarismo_posicao(posicao):
    numero_atual = 1
    total_algarismos = 0
    
    while True:
        # Convertemos o número atual para string para contar seus algarismos
        str_numero_atual = str(numero_atual)
        comprimento_numero = len(str_numero_atual)
        
        # Verificamos se a posição desejada está dentro do número atual
        if total_algarismos + comprimento_numero >= posicao:
            # Calculamos a posição dentro do número atual
            posicao_interna = posicao - total_algarismos - 1
            return str_numero_atual[posicao_interna]
        
        # Atualizamos o total de algarismos contados até agora
        total_algarismos += comprimento_numero
        # Incrementamos o número atual
        numero_atual += 1

# Solicitar ao usuário para inserir a posição desejada
posicao_desejada = int(input("Informe a posição desejada: "))

# Chamando a função para encontrar o algarismo na posição desejada
algarismo = encontrar_algarismo_posicao(posicao_desejada)

print(f"O algarismo que ocupa o {posicao_desejada}º lugar é: {algarismo}")
