def main():
    groceries = []
    while True:
        try:
            item = input("Add to your basket: ").upper()
        except EOFError:
            print()
            break
        else:
            groceries.append(item)
    format_list(groceries)

def format_list(list):
    # alphabetically sorts it and adds how many times you inputted it at the start
    list.sort()
    # other_list is used to make sure theres no duplicates
    other_list = []
    for item in list:
        if item not in other_list:
            other_list.append(item)
    for item in other_list:
        print(f"{list.count(item)} {item}")


main()