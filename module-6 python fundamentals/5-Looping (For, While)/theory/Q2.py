"""
• How loops work in Python.

--> The for loop :
                    the python for loop is more than just a counter-- its and iterator. instead of manually controlling
                    an index,the loop directly goes through each element of an iterable(like list,tuple strings, or even file 
                    objects.)

    How it works : 
                iteration : when you  write a for loop ,python internally calls the iter() function on the iterable. It then uses the 
                it then uses the iterator's __next__() method to fetch each elelment until it rasies a stopiteration exception 
                (which signals the end).

    syntax and indentation : the block of code inside the loop must be indented-- this tells python what's part of loop.

--> The while loop :

                    the while loop continues to execute as long as its condition is true. it's perfect when you don't know in advance 
                    how many times you need to itrate-- just that you need to keep going until the goal is met.

    Howit works :
                    condition based : before every itration, the loop evaluates a condition. if it's true, the loop body executes. if it's
                    false, the loop stops.

                    manual control : with while loop, you often need to update the evaluates the value involved in the condition to avoid
                    creating an infinite loop. 

--> loop control tools :

                    python enhances loop functionality with a few useful keywords : 

                    break : immediately exits the loop.

                    continue : skips to the new iteration.

                    pass: A placeholder that does nothing , its sytacially needed when a statment is required but no action is desired.

                    else : clause on loops : for and while loops can have an else block that runs if the loops completes normally
                           (i.e it wan't terminated by a break). 
"""