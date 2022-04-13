# 04 Un programa que muestre los números perfectos entre 1 y 1000.

# Perfect number, a positive integer that is equal to the sum of its proper
# divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3.

def sum_its_divisors(number):
    addition = 0
    for divisor in range(1, number - 1):
        if number % divisor == 0:
            addition = addition + divisor
    return addition

def get_perfect_numbers(start,end):
    perfect_numbers = []
    for number in range(start,end):
        if sum_its_divisors(number) == number:
            perfect_numbers.append(number)
    return(perfect_numbers)