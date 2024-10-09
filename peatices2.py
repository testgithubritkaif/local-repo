import time
timestamp = time.strftime("%H , %M , %S")
print("Now time continue",timestamp)
hours = int(time.strftime("%H"))
print("Now hour", hours)
Mint = int(time.strftime("%M"))
print("Now Mints", Mint)
second = int(time.strftime("%S"))
print("Now second", second)
if(hours>=0 and hours<12 ):
    print("Good morning")
elif(hours>=12 and hours <17):
    print("Good Afternoon")
elif(hours>=17 and hour):
    print("Good night")
else:
    print("invalid time")
