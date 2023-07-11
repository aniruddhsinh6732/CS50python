while True:
    try:
        str = input("Fraction : ")
        x,y = str.split("/")
        x,y = (int(i) for i in (x,y))
        ans = int(round(x / y,2) * 100)
    except (ValueError,ZeroDivisionError):
        pass
    else:
        if ans == 100:
            print("F")
        elif ans == 0:
            print("E")
        else:
            print(ans,"%",sep="")

        break