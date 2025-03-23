#Generate 20 random integers and store them in a list. Accept a number from the user and print
#position of all occurrences of that number in the list.

import random
lst=[]
for i in range (20):
    lst.append(random.randint(1,10))
print(lst)

