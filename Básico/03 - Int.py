"""Aprendendo o que são números inteiros."""

entrada = input("Digite algo: ")

try:
    numero = int(entrada)
    print("É int (número inteiro).")
except ValueError:
    print("Não é um número inteiro.")

# Int são valores númericos inteiros. Ex: 0,1,2,3,4,5,6,7,8,9....

# Se o número não é inteiro, é float (ponto flutuante).

# Veremos a seguir.