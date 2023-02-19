def menos(letra, numero, alfabeto):
  cont = 0
  numero = int(numero)
  for c in alfabeto:
    if letra == c:
      if cont - numero < 0:
        cont = 26 + (cont - numero)
        return alfabeto[cont]
      else:
        return alfabto[cont - numero]
    cont += 1

def mais(letra, numero, alfabeto):
  cont = 0
  numero = int(numero)
  for c in alfabeto:
    if letra == c:
      if cont + numero > 25:
        cont = (cont + numero) - 26
        return alfabeto[cont]
      else:
        return alfabeto[cont + numero]
    cont += 1

# Variaveis Inicializadas
num = ""
simbolo = ""
resto = ""
palavra = ""
frase = ""
cont = 0
alfabeto = ["a","b","c","d","e","f",
            "g","h","i","j","k","l",
            "m","n","o","p","q","r",
            "s","t","u","v","w","x",
            "y","z"]

# Pedir Valores e Separa-los em Vetores
pal = input()
texto = list(pal)
pal = pal.count("w")
position = []
numero = list(input())

# Montar a Estrutura da soma e subtração da criptografia
for c in numero:
  if "-" in c or "+" in c:
    simbolo = c
    resto = simbolo
  else:
    simbolo = ""
    
  if simbolo == "-" or simbolo == "+":
    num += " " + c
  else:
    num += " " + resto + c + " "
    
num = num.split()
numero = ""

for c in num:
  if c == "+" or c == "-":
    numero += ""
  else:
    numero += " " + c
numero = numero.split()

# Montar a Estrutura do Texto a ser Descriptografado
for i in texto:
  if i == "w":
    position.append(cont)
    palavra += " "
  else:
    palavra += i
  cont += 1

palavra = palavra.split()
texto = ""
cont = 0
for i in palavra:
  if i != " ":
    texto += i
    
# Descriptografar o Texto
for c in numero:
  if "+" in c:
    num = list(c)
    pa = mais(texto[cont], num[1], alfabeto)
    frase += pa
  if "-" in c:
    num = list(c)
    pa = menos(texto[cont], num[1], alfabeto)
    frase += pa
  cont += 1
  
# Inserir Espaços
frase = list(frase)
for i in range(0, pal):
  frase.insert(position[i]," ")
frases = ""
for i in frase:
  frases += i

# Resultado
print(frases)

# Testes

# dqnptacwulwpaq
# -122136+201-31+1-2

# vdwgegewecahiafvmfuv
# -3+159013-2+1-390+99989
