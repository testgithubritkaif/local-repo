# factrorial
def factorial (n):
    if (n==0 or n==1):
        return 1
    else :
        return n*factorial(n-1)
    
# fibonacci    
    
a = int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(a):
    print(f"ansewer of fibonacci : {fibonacci(i)}")    

    
print(f"answer of factrorial : {factorial(5)}")  