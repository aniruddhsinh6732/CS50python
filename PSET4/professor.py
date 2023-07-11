import random


def main():
    level = get_level()
    k = 0
    for i in range(10):
        n = generate_integer(level)
        m = generate_integer(level)
        j = 0
        while True:
            if j == 3:
                print(str(n) + " + " + str(m) + " = " + str(n+m))
                break
            else:
                result = input(str(n) + " + " + str(m) + " = ")
                if result.isdigit():
                    result = int(result)
                    if result != (n+m):
                        print("EEE")
                        j += 1
                        pass
                    else:
                        k += 1
                        break
                else:
                    print("EEE")
                    j += 1
                    pass
    print("Score :",k)
        

def get_level():
    while True:
        lev = int(input("Level : "))
        if lev == 1 or lev == 2 or lev == 3 :
            break
        else:
            pass
    return lev


def generate_integer(level):
    match level:
        case 1:
            num = random.randint(1,10)
        case 2:
            num = random.randint(1,100)
        case 3:
            num = random.randint(1,1000)
    return num
    


if __name__ == "__main__":
    main()