"""model for aircraft flights with food"""

class Flight:

    def __init__(self, number, food):
        
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"First two letters must be upper '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalide route number '{number}'")
   
        #print(number[:])
        self._number = number
        self._food = food

    def number(self):
        return self._number

    def airlane(self):
        return self._number[:2]

    def airplaneFoodName(self):
        return self._food.name()


class Food:

    def __init__(self, name, calories, tastyLevel):
        self._name = name
        self.calores = calories
        self._tastyLevel = tastyLevel

    def name(self):
        return self._name
    
    def calories(self):
        return self._calories


f = Flight("SN090", Food("banana", 500, 5))
print(f.airplaneFoodName())



