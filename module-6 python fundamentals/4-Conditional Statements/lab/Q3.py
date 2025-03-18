"""• Practical Example 7: Write a Python program to calculate grades based on percentage using
    if-else ladder.
"""
percentage = float(input("enter your percentage : "))

if percentage<=100 and percentage>=90:
    print("A")
elif percentage<=90 and percentage>=60:
    print("B")
elif percentage<=60 and percentage>=35:
    print("C")
else:
    print("FAIL")
