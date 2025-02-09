cost = 50
# outside main to make it global (accessible to everything) (idk if this is good or bad to do)
# and also to make it start at 50 and not get reset

def main():
    while True:
        amount = amount_due(insert_coin())
        if int(amount) > 0:
            print("Amount Due: " + str(amount))
            continue
        else:
            print("Change Owed: " + str(amount).replace("-", ""))
            break


def insert_coin():
    while True:
        coin = int(input("Insert coin: "))
        match coin:
            case 5:
                return coin
            case 10:
                return coin
            case 25:
                return coin
            case _:
                return 0

def amount_due(inserted):
    global cost
    #say global to edit a global variable 

    due = cost - inserted
    cost = cost - inserted
    return due

main()