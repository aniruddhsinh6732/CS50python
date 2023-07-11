def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    size = len(s)
    notts = [" ",".",","]

    if 2 > size > 6:
        return False
    
    first = s[:3]

    if not first.isalpha():
        return False

    for i in range(size):
        for nott in notts:
            if s[i] == nott:
                return False
    
    return True
    
    
        
main()