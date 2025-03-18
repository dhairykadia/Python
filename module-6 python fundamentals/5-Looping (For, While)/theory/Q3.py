"""
• Using loops with collections (lists, tuples, etc.).

1) purpose of using loops with collctions:

                colloctions  like lists and tuple store multiple element in a variable.

                loops help to iterate through these collections, making it possible to process,modify or anlyze each
                element without writing repitive code manually.

2) Types of loops for iteration 

                for loop : A common choice for iterating through the elements of a collection. it automatically picks each item one
                           by one.

                while loop : can also be used,through it requires manual indexing and collection to prevent infinite looping.

3) Benifits 

                Automates tasks on large collections.

                simplifies opreations like searching, filtering, aggregating or transforming data.

                Enhances code readablity and maintainbility.

4) Iterating over list 

                e.g. number = [1,2,3,4,5]
                        for number in number:
                            print(numnber) # output each number
                
5) iterating over tuples

                works similarly to list, but tuple are immutable.

                e.g. coordinates = (10,20,30)
                for point in coordinates:
                    print(point) # output each coordinates

6) Enumarating with index 

                somtimes , the index of element is also required. the enumarate() function is handy for this.

                e.g. fruits = ['apple','banana','cherry']
                    for index,fruits in enumerate(fruits):
                        print(f"index: {index}, fruit: {fruit}")

7) Nested loops 
                
                Useful for collection of collections ,such as lists or lists.

                e.g. matrix = [[1,2],[3,4]]
                for row in matrix:
                    for item in row:
                        print(item)
                
8) Using while loop 

                A while loop with collections usually requires indexing.

                e.g. i = 0
                    while i < len(numbers):
                    print(number[i])
                    i += 1
"""