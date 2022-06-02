def main():
    a = input()
    set1 = set(input().split())
    b = input()
    set2 = set(input().split())
    
    dif1 = set1.difference(set2)
    dif2 = set2.difference(set1)

    result = sorted(map(int,dif1.union(dif2)))

    return result

if __name__ == '__main__':
    for value in main():
        print(value)
