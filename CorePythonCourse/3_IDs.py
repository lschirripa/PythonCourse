def main():
    a = 5
    print(a)
    b = a
    b = 6
    print(a)

def list():
#value-equity and identity are fundamentally different concepts

    listA = [1,2,3]
    listB = [1,2,3]

    print(listA == listB)
    print(listA is listB) #checks if id() are equals

#main()
list()