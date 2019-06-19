# Binary search - search element in a list
import random
listn=sorted(random.sample(range(100),10))
print(listn)
num=int(input("Enter a number to be searched in list: "))

def search(listn,num):
    
    while len(listn)//2 >=1:
        midnum=len(listn)//2
        print(midnum)
        if listn[midnum] == num:
            return True
        elif num > listn[-1]:
            return False
        elif num < listn[midnum]:
            listn=listn[:midnum]
            print("1")
            print(listn)
        elif num > listn[midnum]:
            listn=listn[midnum:]
            print(listn)
        else:
            return False

if search(listn,num):
    print("Number is in list")
else:
    print("Number is not in list")
