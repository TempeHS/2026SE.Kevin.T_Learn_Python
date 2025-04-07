import sys
import csv

if len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit()
elif len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit()

try:
    open(sys.argv[1])
except FileNotFoundError:
    print("File not found")
    sys.exit()


with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first, last = row["name"].split(", ")
            house = row["house"]
            writer.writerow({"first": first, "last": last, "house": house})