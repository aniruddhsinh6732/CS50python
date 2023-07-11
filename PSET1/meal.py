def main():
    time = input("What time it is? ")
    t2 = convert(time)

    if 7.0 <= t2 <= 8.0:
        print("breakfast time")
    elif 12.0 <= t2 <= 13.0:
        print("lunch time")
    elif 18.0 <= t2 <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    h,m = time.split(":")
    h = int(h)
    m = int(m)
    m = m / 6
    if m == 10 : 
        h = h + 1
    h = h * 100
    m = m * 10
    temp = float(h + m)
    return temp/100
    

main()