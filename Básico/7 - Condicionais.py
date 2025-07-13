periodo = input("Está claro ou escuro? ")

if periodo == "claro" or periodo == "CLARO":
    print("Está de dia.")
elif periodo == "escuro" or periodo == "ESCURO":
    print("Está de noite.")
else:
    print("Erro! Ou está de dia ou de noite, tente novamente.")

# If, elif e else propõe condições no código.
# No exemplo acima temos um script de período do dia.

# If determina "se". Então, se estiver claro, está de dia, caso contrário, é noite.

# Elif é caso se você for colocar outro if.

# Else é usado caso as outras as opções não forem correspondidas. 