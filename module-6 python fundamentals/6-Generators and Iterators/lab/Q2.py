"""
• Write a Python program that uses a custom iterator to iterate over a list of integers.
"""
class CustomIterator:
    def _init_(self,numbers):
        self.numbers=numbers
        self.index=0

    def _iter_(self):
        return self 
    
    def _next_(self):
        if self.index<len(self.numbers):
            value=self.numbers[self.index]
            self.index +=1
            return value 
        else : 
            raise StopIteration
        
number_list=[10,20,30,40,50]

custom_iter=CustomIterator(number_list)

print("Iterating over the list : ")
for number in custom_iter:
    print(number)