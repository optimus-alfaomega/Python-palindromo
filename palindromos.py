print ("PALINDROMOS \n")

mensaje = input("escriba una palabra \n")
pal=""
palR=""

mensaje =mensaje.lower()

for letra in mensaje:
    if not letra.isalpha():
            continue
    pal +=letra 

for letra in reversed(pal):
    palR +=letra

if pal == palR:
    print ("es palindromo")
else:
    print("no es palindromo")


