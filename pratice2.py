import time
hours= int(input ("enter your hours"))
timestamp=time.strftime('%H:%M:%S')
hours=int(time.strftime('%H'))
Mint=time.strftime('%M')
print(Mints)
Second=time.strftime('%S')
if (hours>=0 and hours<12):
    print("good morning")
elif(hours>=12 and hours<17):
    print("good evening SIR")
elif(hours>=17 and hours<24):
    print("good night sir")
else:
    print("invalid input")    



