import inflect
inflect = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input("Name: ").title()
        except EOFError:
            print()
            break
        else:
            names.append(name)
    print(adieu_er(names))

def adieu_er(names):
    return "Adieu, Adieu, to " + inflect.join(names) #mayne it wasnt that complicated

main()