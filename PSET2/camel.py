def main():
    camel = input("camelCase : ")
    snake = underscore(camel)
    print("snake_case :",snake)

def underscore(str):
    for i in range(len(str)):
        if str[i].isupper():
            first = str[:i+1]
            second = str[i+1:]
            first = first.lower()
            str = first + second
            str = str[:i] + "_" + str[i:]
    return str

main()