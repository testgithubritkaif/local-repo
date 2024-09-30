def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("average", (sum)/len(numbers))
        
average(2,6,4,4)        