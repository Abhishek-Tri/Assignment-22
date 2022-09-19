#Write a recursive python function to calculate sum of first N natural numbers

def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)    

num=int(input("Enter a number :"))
r=sumN(num)
print("sum of natural numbers is :",r)

