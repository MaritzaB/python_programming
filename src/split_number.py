# Un programa que lea un número entero de 3 cifras y muestre por separado las
# cifras de ese número

while True:
    number = str(input("\n Please, enter a number of 3 digits: \n"))
    if len(number) != 3:
        print("The number you've entered doesn't have 3 digits")
    else:
        print(f"The digits of the number are: {number[0]}, {number[1]} and {number[2]} \n")
        break
