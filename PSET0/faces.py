def main():
    str = input("enter string : ")
    str = convert(str)
    print(str)

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()