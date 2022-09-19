#Write a recursive python function to print binary of a given decimal number.

def printbin(n):
    if n>0:
        printbin(n//2)
        print(n%2,end='')

num=int(input("Enter a number :"))
print("binary of" ,num, "is :")
printbin(num)
       