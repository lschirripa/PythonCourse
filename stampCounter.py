from turtle import stamp


def main():
    quant = int(input())
    stampsSet = set()
    for n in range(0,quant):
        stampsSet.add(input())

    totalValue = len(stampsSet)
    
    return totalValue
        

if __name__ == '__main__':
    print(main())
