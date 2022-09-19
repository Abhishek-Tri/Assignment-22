# Write a recursive python function to find the Nth term of the Fibonacci series

def fab(n):
    if n<=1:
        return n
    return fab(n-1)+fab(n-2)  

num=int(input("Enter a number :"))
print(num,"th term of fabonacci series is :",fab(num))
       