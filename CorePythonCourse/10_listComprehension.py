from math import factorial

def auxFunction_that_do_the_same_(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def main():
    words = "this is a test".split()

    words_lenMapped = [len(word) for word in words]

    print(words)
    print(words_lenMapped)
    print(auxFunction_that_do_the_same_(words))
    print("------------------------------")
    f = [len(str(factorial(x))) for x in range(20)] # -> could be replaced with {} as a set
    print(f)

main()

#COMPREHENSION -> [expr(item) for item in iterable]