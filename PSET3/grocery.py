def edit_list(items):
    new_items= []
    for i in range(len(items)):
        found = False
        for j in range(i+1,len(items)):
            if items[i]["item"] == items[j]["item"]:
                items[i]["value"] += 1
                found = True
        if not found:
            new_items.append(items[i])
    
    return new_items

def main():
    items = []

    while True:
        try:
            it = input()
            item = {"item": it , "value" : 1}
            items.append(item)

        except KeyboardInterrupt:
            it = edit_list(items)
            for item in it:
                print(item["value"],item["item"].upper())
            break
        else:
            pass


main()