menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    items = []
    while True:
        try:
            item = input("Order a: ").title()
        except EOFError:
            print()
            break
        else:
            items.append(item)

    calculate_cost(items)

def calculate_cost(items):
    costs = []
    for item in items:
        if item in menu:
            costs.append(menu[item])
        else:
            pass

    cost = 0
    for number in costs:
        cost += number
    
    print(f"Total: ${cost:.2f}")

main()