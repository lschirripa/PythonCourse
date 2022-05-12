"""model for aircraft flights"""

class Flight:

    def __init__(self, number):
        
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"First two letters must be upper '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalide route number '{number}'")
   
        #print(number[:])
        self._number = number

    def number(self):
        return self._number

    def airlane(self):
        return self._number[:2]


f = Flight("SN090")
print(f.number())

