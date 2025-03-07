num1 = float(input("Num 1: "))
num2 = float(input("Num 2: "))
operator = input("Operator: ")
ui_output = ""

if operator == "+":
    ui_output = num1 + num2
elif operator == "-":
    ui_output = num1 - num2
elif operator == "*":
    ui_output = num1 * num2
elif operator == "/":
    ui_output = num1 / num2
else:
    print("Not a known operator")

print(float(ui_output))