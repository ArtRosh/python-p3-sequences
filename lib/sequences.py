#!/usr/bin/env python3

def print_fibonacci(length):
    number = []
    if(length == 0):
        print(number)
    elif(length == 1):
        number.append(0)
        print(number)
    elif(length == 2):
        number.append(0)
        number.append(1)
        print(number)
    elif(length >= 2):
        number.append(0)
        number.append(1)
        while(length > len(number)):
            number.append(number[-1] + number[-2])
        print(number)