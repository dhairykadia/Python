"""
• Write a generator function that generates the first 10 even numbers.
"""

def generateEvennumbers():
    num = 2
    count = 0
    while count<10:
        yield num 
        num+=2
        count+=1
for even in generateEvennumbers():
    print(even)