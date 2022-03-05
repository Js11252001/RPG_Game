import random
list = []
for i in range(10):
    # print(i, end=", ")
    list.append(random.randrange(100)) # Integer from 0 to 99 inclusive
    
print(list)