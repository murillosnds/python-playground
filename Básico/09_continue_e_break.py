"""Aprendendo o que faz continue e break."""

seguidores = 1
while seguidores < 100:
    seguidores += 1
    if seguidores == 50:
        continue
    print(seguidores)

# Aqui usamos while (enquanto) e continue (continuar).
# A variável seguidores armazena o valor 1
# e enquanto o números de seguidores for menor que 100 é somado de 1 em 1.
# Se o número de seguidores for igual a 50, o código continuará.
# Por fim é impresso o número de seguidores.

seguidores = 1
while seguidores < 100:
    seguidores += 1
    if seguidores == 50:
        break
    print(seguidores)

# Agora neste aqui acontence o contrário.
# Quanto atigir exatos 50 seguidores o código quebra e voltando para o começo.
