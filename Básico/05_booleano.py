"""Aprendendo o que são operadores booleanos em Python."""

entrada = input("Digite algo: ")

if entrada.lower() == "true":
    print("É booleano! É Verdadeiro.")
elif entrada.lower() == "false":
    print("É booleano! É Falso.")
else:
    try:
        valor = int(entrada)
        print("Não é booleano! É int (número inteiro).")
    except ValueError:
        try:
            valor = float(entrada)
            print("Não é booleano! É float (número com ponto).")
        except ValueError:
            print("É uma string.")

# Aqui é feito uma verificação se é float, booleano, int ou string.
