import random
listn=random.sample(range(100),10)
num=input("Enter a number to be searched in list: ")

if num in listn:
    print(num+" is present in list")
else:
    print(num+" is not present in list")
