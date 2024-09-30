kaif=[1,2,5,6,3,4,7,10,0,9,8]
# print(max(kaif))
max=kaif[0]
for number in kaif:
    if(number > max):
        max=number
print(max)        
# mimimum
min1=kaif[10]
for num in kaif:
    if(num < min1):
        min1=num
print(min1)        