#Write a recursive python function to calculate sum of first N odd natural numbers

def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-2)    

num=int(input("Enter a number :"))
r=sumN(num*2-1)
print("sum of" ,num, "odd natural numbers is :",r)
