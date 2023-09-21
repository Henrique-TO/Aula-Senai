numeros= [1,2,3,4,5]
print(numeros)

#2
print(numeros[2])

#3
numeros.append(6)
print(numeros)

#4
numeros.remove(3)
print(numeros)

#5
frutas= ['maça','banana','laranja']
lista= numeros + frutas
print(lista)

#6
for fruta in frutas:
    print(fruta)

#7
if 5 in lista:
    print('tem 5 na lista')
else:
    print('Não tem 5 na lista')
