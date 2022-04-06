# 05 Un programa para contar el número de palabras en una frase.

# quote = str(input("Please enter you quote: \n"))


def word_counter(quote):
    quote = str(quote)
    n_words = len(quote.split())
    return n_words


# print(f"Your quote has {word_counter(quote)} words \n")
