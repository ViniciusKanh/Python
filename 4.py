def completar_sequencias():
    # a) Sequência de números ímpares
    seq_a = [1, 3, 5, 7]
    seq_a.append(9)  # Próximo número ímpar
    print(f"a) {seq_a}")

    # b) Sequência de potências de 2
    seq_b = [2, 4, 8, 16, 32, 64]
    seq_b.append(128)  # Próxima potência de 2
    print(f"b) {seq_b}")

    # c) Sequência de quadrados perfeitos
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    seq_c.append(49)  # Próximo quadrado perfeito
    print(f"c) {seq_c}")

    # d) Quadrados perfeitos de números pares
    seq_d = [4, 16, 36, 64]
    seq_d.append(100)  # Próximo quadrado perfeito de número par
    print(f"d) {seq_d}")

    # e) Sequência de Fibonacci
    seq_e = [1, 1, 2, 3, 5, 8]
    seq_e.append(13)  # Próximo número de Fibonacci
    print(f"e) {seq_e}")

    # f) Sequência alternando múltiplos de 2 e não múltiplos de 3
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    seq_f.append(20)  # Próximo número que não é múltiplo de 3
    print(f"f) {seq_f}")

completar_sequencias()
