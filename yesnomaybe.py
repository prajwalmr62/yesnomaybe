#prajwal
#yes or no!
import random

i=random.randrange(1,1000000)
print ("Ask your Question!")
inp=raw_input("Now press enter")
print (i)
if (i%7):
    if not(i%5):
        print ("NO")
    elif (i%(i+20)):
        print ("YES")
elif not(i%34):
    if (i%76):
        print ("YES")
    else :
        print ("NO")
else :
    print ("May Be?!")
