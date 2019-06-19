import random
listn=sorted(random.sample(range(100),10))
num=input("Enter a number to be searched in sorted list: ")

print(listn)

if num in listn:
    print(num+" is present in list")
else:
    print(num+" is not present in list")
