def first(iterable):
    iterator = iter(iterable)
    try:
         next(iterator) # THIS IS THE FIRST ITER
         next(iterator) 
         next(iterator)
         return next(iterator) 
    except StopIteration:
        raise ValueError("iterable is empty")


def main():

    iterable = ["one", "two", "three", "four"]
    print(first(iterable))

    # i could also use:
    print(first(iterable))
    # and also with sets

main()



