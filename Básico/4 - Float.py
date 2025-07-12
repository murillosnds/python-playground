entrada = input("Digite algo: ")

try:
    numero = int(entrada)
    print("Não é float! É um número inteiro")
except ValueError:
    try:
        valor = float(entrada)
        print("É float (número com ponto).")
    except ValueError:
        print("Não é float. É string.")

# Float é um número com ponto. Ex: 4.9, 7.4, 10.0.

# Se o número não tem ponto. É int (inteiro).