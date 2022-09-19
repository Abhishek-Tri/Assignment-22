#Write a recursive python function to calculate the factorial of a number.

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)    

num=int(input("Enter a number :"))
r=fact(num)
print("factorial of" ,num, "is :",r)