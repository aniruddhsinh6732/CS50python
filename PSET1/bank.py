str = input("Greeting : ")

def checkHello(string,word):
    if word in string:
        return 1
    else:
        return 0


if checkHello(str,"Hello"):
    print("$0")
elif str.startswith("H"):
    print("$20")
else :
    print("$100")

