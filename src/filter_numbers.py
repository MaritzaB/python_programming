# 10 Un programa que lee un archivo de texto que contiene palabras y números
# enteros, se deben mostrar únicamente los números en la pantalla.

file_name = "./data/demo_file.txt"
demo_file = open(file_name, "r")

print(demo_file.read())