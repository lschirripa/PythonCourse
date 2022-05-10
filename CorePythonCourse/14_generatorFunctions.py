def gen246():
    print("about to yield 2")
    yield 2
    print("about to yield 4")
    yield 4
    print("about to yield 6")
    yield 6
    print("about to return")

g = gen246()

next(g)
next(g)
next(g)
next(g)