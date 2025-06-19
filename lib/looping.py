#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
        if i == 0:
            print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_int_list = [integer * integer for integer in int_list]
    return squared_int_list

def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if (i % 3 == 0) and (i % 5 == 0):
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (f"{i}")
        i += 1
