#Write a recursive python function to calculate sum of the digits of a given number

def sumofdigit(n):
    if n==0:
        return 0
    return (n%10)+sumofdigit(n//10)
        

num=int(input("Enter a number :"))
r=sumofdigit(num)
print("sum of digits of" ,num, "is :",r)
