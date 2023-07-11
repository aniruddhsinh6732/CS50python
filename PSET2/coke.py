def main():
    due = 50
    while True:
        print("Amount Due :",due)
        insert = int(input("Insert Coin : "))
        due = due - insert
        if due <= 0:
            break
    print("Change Owed :",due)


main()