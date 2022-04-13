# 07 Un programa para convertir un entero en decimal a binario en forma recursiva e
# iterativa.

number = 0
lista=[number]
while number>1:
  quotient = int(number/2)
  number = quotient
  lista.append(number)
  if quotient == 1:
    break
lista.reverse()
print(*lista)

binary_set = []
for index,element in enumerate(lista):
  if element % 2 == 0:
    binary_set.append(0)
  else:
    binary_set.append(1)

print(*binary_set)
  