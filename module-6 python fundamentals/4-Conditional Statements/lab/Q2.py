"""
• Practical Example 6: Write a Python program to check if a number is prime using if_else.
"""

num = int(input("enter a number"))

if num > 1:
    for i in range(2,int(num ** 0.5)+1):
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")


