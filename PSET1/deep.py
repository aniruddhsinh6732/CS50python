answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

match answer:
    case "42" | "Forty Two" | "forty-two" :
        print("Yes")
    case _:
        print("No")