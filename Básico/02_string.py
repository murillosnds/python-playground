"""Aprendendo o que string."""

entrada = input("Digite algo: ")

try:
    numero = float(entrada)
    print("Não é uma string! É um número")
except ValueError:
    print("É uma string.")

# String são valores cercados por "" (aspas simples ou duplas).

# Algo que não é string. Pode ser número, booleano ou float.
