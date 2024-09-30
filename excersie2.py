print(f"Kaun Banega Crorepati")
questions=[["most famous languagle is", "php","java","c++","python","html",4 ] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,
["which laguagr use for website","html" ,"css" , "all" , "java script",4] ,]

level = [1000,2000,5000,10000,50000,100000,200000,2600000,5000000,7500000,100000000]
money = 0
for i in range(0, len(questions)):
    question=questions [i]
    print(f"\n \n question for Rs:.{level[i]}")
    print(f"question = .{question[0]}")
    print(f"a.{question[1]}                        b.{question[2]}")
    print(f"c.{question[3]}                        d.{question[4]}")
    reply=int(input("Enter your answer "))
    if (reply == 0 ):
        print("you use to quit life line")
        break
    if(reply==question[-1]):
        print(f"your answer is correct. {level[i]}")
        if(i==4):
            money== 50000
        elif(i==8):
            money= 2600000
        elif(i==11):
            money= 100000000     
    else:
        print("worng answer")
        break
print(f"YOU GATE TOTAL MONEY is {money} ")
