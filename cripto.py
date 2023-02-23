from random import randrange

def mais(alfabeto,letra):
    global num
    cont = 0
    for i in alfabeto:
        if letra == i:
            if alfabeto[cont - num] == "w":
                if num > 0:
                    num -= 1
                else:
                    num += 1
            return alfabeto[cont - num]
        cont += 1

def menos(alfabeto,letra):
    global num
    cont = 0
    for i in alfabeto:
        if letra == i:
            if cont + num > 25:
                count = cont + num - 25
            else:
                count = cont + num
            if alfabeto[count] == "w":
                if num > 0:
                    num -= 1
                else:
                    num += 1
            if cont + num > 25:
                return alfabeto[cont + num - 25]
            else:
                return alfabeto[cont + num]
        cont += 1


# Entrada de Dados
texto = input()
alfabeto = ["a","b","c","d","e","f",
            "g","h","i","j","k","l",
            "m","n","o","p","q","r",
            "s","t","u","v","w","x",
            "y","z"]
texto = list(texto)
count = 0
palavra = ""
numero = ""


# Quantidade de Letras
for c in texto:
    count += 1

# Criptografando
for i in range(count):
    simbolo = randrange(2)
    if texto[i] != " ":
        if simbolo == 0:
            simbolo = "+"
            num = randrange(10)
            pa = mais(alfabeto,texto[i])
            nume = simbolo + str(num)
        else:
            simbolo = "-"
            num = randrange(10)
            pa = menos(alfabeto,texto[i])
            nume = simbolo + str(num)
        numero += nume
    else:
        pa = "w"
    palavra += pa

# Tratamento de Dados dos numeros
nume = list(numero)

count = 0
for c in nume:
    count += 1

i = count-1
while(i > 0):
    if nume[i] == "+" or nume[i] == "-":
        if nume[i] == nume[i-2]:
            del nume[i]
    i = i-1

# Juntando os Numeros
numero = ""
for i in nume:
    numero += i
    
# Resultados
print(palavra)
print(numero)
