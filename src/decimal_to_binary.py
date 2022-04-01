# 07 Un programa para convertir un entero en decimal a binario en forma recursiva e
# iterativa.


"""
# codigo de Cirse López
import time

def dec_bin(n):
  digitos = list() #Definimos una lista vacia
  if n<2: #Caso trivial
    digitos.append(n)
  else :
    a=n%2 #ultimo digito
    digitos.append(a) #Lo guarda en la lista hasta el final
    n=int((n-a)/2) # Calcula el numero sin el ultimo digito
    digitos.extend(dec_bin(n)) #Junta los elementos de las listas
  
  return(digitos)

n = int(input("Numero decimal:> "))

# Con funcion recursiva
inicio_rec = time.time_ns()
digitos = dec_bin(n)
fin_rec = time.time_ns()
di
"""
