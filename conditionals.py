temperature = int(input("type the temperature \n"))
raining = True

if temperature < 70 and not raining:
    print("go outside")
else:
    print("dont go outside")