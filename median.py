"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()

size = len(numbers)
if size%2 == 1: 
    print(numbers[int((size-1)/2)])
else: 
    print((numbers[int(size/2)]+numbers[int((size/2)-1)])/2)
