#Write a recursive python function to print octal of a given decimal number

def printoct(n):
    if n>0:
        printoct(n//8)
        print(n%8,end='')

num=int(input("Enter a number :"))
print("octal of" ,num, "is :")
printoct(num)
       