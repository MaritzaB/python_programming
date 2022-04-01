# Un programa para contar el número de palabras en una frase.

quote = str(input("Please enter you quote: \n"))

n_words = len(quote.split())

print(f"Your quote has {n_words} words \n")
