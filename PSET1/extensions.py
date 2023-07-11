file = input("file name : ")

first,last = file.split(".")

match last:
    case "gif"|"jpg" |"jpeg"|"png":
        print("image/"+ last)
    case "pdf"|"txt"|"zip":
        print("application/" + last)
    case _:
        print("application/octet-stream")