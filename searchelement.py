# Search element in a list
import random
listn=sorted(random.sample(range(100),10))
print(listn)
num=int(input("Enter a number to be searched in list: "))

def search(listn,num):
    for n in listn:
        if n == num:
            return True
            
    return False

if search(listn,num)==True:
    print("Number is in list")
else:
    print("Number is not in list")
