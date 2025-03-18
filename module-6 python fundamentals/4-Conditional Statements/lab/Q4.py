"""
• Practical Example 8: Write a Python program to check if a person is eligible to donate blood
using a nested if.

"""
age = int(input("enter your age"))
weight = int(input("enter your weight"))

if age>18:
    if weight>50:
        print("you are eligble to donate blood")
    else:
        print("you are not eligble to donate blood")
else:
    print("you are underage and not eligble to donate blood")