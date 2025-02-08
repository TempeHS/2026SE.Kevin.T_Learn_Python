expression = input("Expression: ").split()

x = int(expression[0])
operator = expression[1]
y = int(expression[2])

if operator == "+":
    thing = x + y
elif operator == "-":
    thing = x - y
elif operator == "*":
    thing = x * y
elif operator == "/":
    thing = x / y

print(float(thing))
# 9 errors for what it works