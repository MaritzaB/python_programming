# 06 Un programa que pueda calcular el cociente de dos números enteros en forma
# recursiva e iterativa.

def divide_two_numbers(dividend,divisor):
    pairs = []
    while True:
        quotient = int(dividend/divisor)
        remainder = dividend % divisor
        dividend = quotient
        divisor = remainder
        pairs.append([dividend,divisor])
        if remainder == 0 or dividend<divisor:
            break
    return pairs

print(divide_two_numbers(77,9))
