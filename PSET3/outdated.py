months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date : ")
        if date.isdigit():
            m,d,y = date.split("/")
        else:
            date = date.replace(",","")
            m,d,y = date.split(" ")
            d = int(d)
    except ValueError:
        pass
    else:
        if not m.isdigit():
            new_m = 1
            for i in months:
                if m == i:
                    break
                else:
                    new_m += 1
            m = new_m
        else:
            m = int(m)

        break
         
if d < 10 :
    new_d = "0" + str(d)
    d = new_d
    
if m < 10 :
    new_m = "0" + str(m)
    m = new_m

print(y,m,d,sep="-")