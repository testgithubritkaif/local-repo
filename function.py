def calmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def greaternum(a,b):
    if(a>b):
        print("1st num greater")
    else:
       print("2nd num greater")  
def lessnum(a,b):
    if(a<b):
        print("num 1 less") 
    else:
        print("2nd num less")                
a=5
b=7
c=int(input("enter num"))
d=int(input("enter num"))
calmean(a,b)
greaternum(a,b)   
lessnum(a,b)
calmean(c,d)
greaternum(c,d)   
lessnum(c,d)
