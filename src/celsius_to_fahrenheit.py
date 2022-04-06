# 01 Programa que lea un dato de tipo float que contenga una cantidad de grados
# centígrados para que mediante la aplicación de la fórmula F=32+(9*C/5),
# convierta esa cantidad a grados Fahrenheit.

# print("Please introduce the temperature in degrees Celsius: \n")
def ask_a_number():
    degrees_celsius = input("Please, enter a temperature")
    return degrees_celsius


def convert_celsius_to_fahrenheit(degrees_celsius):
    degrees_celsius = float(degrees_celsius)
    degrees_fahrenheit = 32 + (9 * degrees_celsius / 5)
    return degrees_fahrenheit


# print(f"The temperature in degrees fahrenheit is {convert_celsius_to_fahrenheit(degrees_celsius)}")
