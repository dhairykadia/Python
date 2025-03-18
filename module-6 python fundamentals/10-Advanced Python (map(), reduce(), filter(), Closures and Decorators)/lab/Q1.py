"""
• Write a Python program to apply the map() function to square a list of numbers.

"""

number = [1,2,3,4,5]
squard_number = list(map(lambda x: x**2,number))
print("original list",number)
print("Squard number:",squard_number)