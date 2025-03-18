"""
• Write a Python program that filters out even numbers using the filter() function.

"""

number = [1,2,3,4,5,6,7,8,9,10]

odd_number = list(filter(lambda x: x % 2 != 0,number))

print("original list",number)
print("odd number",odd_number)