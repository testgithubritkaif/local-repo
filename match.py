ka = int(input("enter you num :"))
match ka:
    case 0:
        print("your num is zero")
    case _ if ka!=90:
        print(ka,"is not equal to 90")
    case _ if ka!=80:
        print(ka,"is not equal to 80")
    case _:
        print(ka)