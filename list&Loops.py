list = ['boca','river','lanus']

print(list)

list.append(5)

list.remove(list[0])

del list[0]

print(list)

if 5 in list:
    list.append('banfield')
else:
    list.append('gimnasia')

print(list)

stringTest = "banfield"

if stringTest in list:
    print('banfield is in the list')

for Element in list:
    print(Element)