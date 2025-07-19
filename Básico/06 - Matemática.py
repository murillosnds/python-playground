"""Aprendendo como fazer operações matemáticas em Python."""

numero_1 = int(float(input("Digite um número: ")))
numero_2 = int(float(input("Digite um número: ")))
tipo = input("Qual tipo de operação deseja fazer? ( + | - | * | / | ** | % ): ")

soma = numero_1 + numero_2
subtração = numero_1 - numero_2
multiplicação = numero_1 * numero_2
divisão = numero_1 / numero_2
potenciação = numero_1 ** numero_2
resto_da_divisao = numero_1 % numero_2

if tipo == "+":
    print(f"O resultado de {numero_1} + {numero_2} é {soma}.")
elif tipo == "-":
    print(f"O resultado de {numero_1} - {numero_2} é {subtração}.")
elif tipo == "*":
    print(f"O resultado de {numero_1} x {numero_2} é {multiplicação}.")
elif tipo == "/":
    print(f"O resultado de {numero_1} / {numero_2} é {divisão}.")
elif tipo == "**":
    print(f"O resultado de {numero_1} ** {numero_2} é {potenciação}.")
elif tipo == "%":
    print(
        f"O resultado do resto da divisão de {numero_1} / {numero_2} é {resto_da_divisao}."
    )

# Em python é possível realizar contas matématicas como adição, subtração, divisão, multiplicação e potenciação.

# Adição = +
# Subtração -
# Multiplicação = *
# Divisão = /
# Divisão inteira = //
# Potenciação = **
# Resto da divisão = %
