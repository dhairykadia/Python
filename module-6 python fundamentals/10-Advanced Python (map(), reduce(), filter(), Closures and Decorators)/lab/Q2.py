"""
• Write a Python program that uses reduce() to find the product of a list of numbers.

"""
from functools import reduce

number = [1,2,3,4,5]

product = reduce(lambda x,y : x * y ,number)

print("original list :",number)

print("product of the list:",product)