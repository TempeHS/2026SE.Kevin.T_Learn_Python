def main():
    while True:
        fuel = input("Fuel: ")
        try:
            fuel_percent = fraction_to_percent(fuel)
        except (ValueError, ZeroDivisionError):
            pass
        if fuel_percent == None:
            pass
        else:
            break

    if fuel_percent >= 99:
        print("F")
    elif fuel_percent <= 1:
        print("E")
    else:
        print(str(fuel_percent) + "%")


def fraction_to_percent(fraction):
    split = fraction.split("/")
    x = int(split[0])
    y = int(split[1])

    if x > y:
        return 

    return int((x / y) * 100)

main()