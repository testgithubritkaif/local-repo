import time
hours= int(input ("enter your hours"))
print(hours)
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
# hours=int(time.strftime('%H'))
print(hours)
Mints=time.strftime('%M')
print(Mints)
Second=time.strftime('%S')
print(Second)
if (hours>=0 and hours<12):
    print("good morning")
elif(hours>=12 and hours<17):
    print("good evening SIR")
elif(hours>=17 and hours<0):
    print("good night sir")



