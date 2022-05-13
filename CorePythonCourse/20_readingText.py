g = open("test.txt", mode="rt", encoding="utf-8")

print(g.read(10))

g.seek(0)

print(g.read())

#readline reads the first line

for i in range(20):
    print('---',end="")

print("\n")

g.seek(0)

print(g.readline())

# if i call readline again it reads the file until the next \n

print(g.readline())
print(g.readline())

#now lets do readlines() -> bring me all in a list

for i in range(20):
    print('---',end="")

print("\n")


g.seek(0)

print(g.readlines())