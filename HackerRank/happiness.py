def main():
    a = input()
    commonList = set(map(int,input().split()))
    setA= set(map(int,input().split()))
    setB = set(map(int,input().split()))
    happiness = 0

    for value in commonList:
        if value in setA:
            happiness += 1

    for value in commonList:
        if value in setB:
            happiness -= 1

    print(happiness)

        

if __name__ == '__main__':
    main()
