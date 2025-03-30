import sys
import csv
import tabulate

if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit()

if not sys.argv[1].endswith(".csv"):
    print("Not a .csv file")
    sys.exit()

try:
    open(sys.argv[1])
except FileNotFoundError:
    print("File not found")
    sys.exit()

table = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)

    for row in reader:
        table.append(row)

print(tabulate.tabulate(table, headers="keys", tablefmt="grid"))