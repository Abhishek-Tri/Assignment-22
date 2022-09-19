#Write a recursive python function to calculate sum of first N even natural numbers

def sumN(n):
    if n==2:
        return 2
    return n+sumN(n-2)    

num=int(input("Enter a number :"))
r=sumN(num*2)
print("sum of" ,num, "even natural numbers is :",r)
