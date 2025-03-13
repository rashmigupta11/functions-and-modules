
#Factorial by recursion
n=int(input("Enter a number:"))
def factorial(n):
    if n<2:
        return 1
    else:
        return n* (factorial(n-1))
f=factorial(n)
print("Factorial of ", n, "is: ",f)

#Factorial by for loop

n=int(input("n:"))
fact=1
for i in range(1,n+1):
    fact = fact * i
print(fact)