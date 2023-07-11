def main():
    str = input("Input : ")
    str = shorten(str)
    print("Output :",str)


def shorten(s):
    vowels = ["a","e","i","o","u","A","E","I","U","O"]
    for vowel in vowels:
        s = s.replace(vowel,"")
    return s


if __name__ == "__main__":
    main()