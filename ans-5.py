#Write a recursive python function to calculate sum of cubes of first N natural numbers

def sumN(n):
    if n==1:
        return 1
    return n**3+sumN(n-1)    

num=int(input("Enter a number :"))
r=sumN(num)
print("sum of cube of" ,num, "natural numbers is :",r)
