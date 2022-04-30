#!/bin/python3

import math
import os
import random
import re
import sys

def number_is_odd(value):
    if value%2 != 0:
        return True 
    else:
        return False
        
def range(value):
    if 2 <= value <= 5:
         return "Not Weird"
    if 6 <= value <= 20:
        return "Weird"
    if value > 20:
        return "Not Weird"
    



if __name__ == '__main__':
    n = int(input().strip())
    if number_is_odd(n):
        print("Weird")
    else:
        print(range(n))
    

