def conta_a(texto):
    return texto.lower().count('a')

string = input("Informe uma string: ")
quantidade = conta_a(string)

print(f"A letra 'a' aparece {quantidade} vezes na string informada.")
