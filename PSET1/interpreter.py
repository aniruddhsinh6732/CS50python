exp = input("expression : ")

x,y,z = exp.split(" ")

x = int(x)
z = int(z)

match y :
    case "+":
        ans = x + z
    case "-":
        ans = x - z
    case "*":
        ans = x * z
    case "/":
        if z == 0:
            print("not possible, change value of Z")
        else:
            ans = x / z
    case _:
        print("This operation is not valid")

ans = float(ans)
print(ans)