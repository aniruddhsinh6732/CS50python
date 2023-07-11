names = []
while True:
    try:
        name = input("Name : ")
        names.append(name)
    except KeyboardInterrupt:
        print("\nAdieu, adieu, to ",end="")
        size = len(names)
        match size:
            case 0:
                pass
            case 1:
                print(names[0])
            case 2:
                print(names[0],"and",names[1])
            case _:
                for i in range(size-1):
                    if i == size-2:
                        print(names[i],names[i+1],sep=" and ")
                        break
                    else:
                        print(names[i],end=",")
        
        break


