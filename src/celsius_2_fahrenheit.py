# Programa que lea un dato de tipo float que contenga una cantidad de grados
# centígrados para que mediante la aplicación de la fórmula F=32+(9*C/5),
# convierta esa cantidad a grados Fahrenheit.

print("Please introduce the temperature in degrees Celsius: \n")

degrees_celsius = float(input())

degrees_fahrenheit = 32 + (9 * degrees_celsius / 5)

print(f"The temperature in degrees fahrenheit is {degrees_fahrenheit}")
