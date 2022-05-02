if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split(sep=','))
    # print(*arr)

    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))

    print (max(lis))