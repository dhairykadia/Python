"""
• Write a Python program to sort a list using both sort() and sorted().

"""

list = [10,20,30,40,50]
list.sort()
print(f"list after using sort() {list}")
sortedList = sorted(list,reverse=True)
print(f"list after using sorted() in decending order : {sortedList}")
