import sys

line_count = 0

if len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit()
elif len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit()

if not sys.argv[1].endswith(".py"):
    print("Not a python file")
    sys.exit()

with open(sys.argv[1]) as file:
    for line in file:
        if line.strip(): #checks if its only spaces
            if not line.lstrip().startswith("#"): # if it doesnt start with comment thing add 1
                line_count += 1

print(f"{sys.argv[1]} has {line_count} lines")