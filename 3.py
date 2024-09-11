def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    while K <= INDICE:  # Continua até que K seja igual a INDICE
        K += 1          # Incrementa K antes de somar em SOMA
        SOMA += K       # Soma o valor de K em SOMA
    return SOMA

soma_resultado = calcular_soma()
print(f"O valor final da variável SOMA é: {soma_resultado}")
