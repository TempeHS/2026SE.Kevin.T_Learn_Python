from pyfiglet import Figlet
import sys
figlet = Figlet()

def invalid():
    print("invalid usage")
    sys.exit()

#figlet.setFont(font="usa_____")
if len(sys.argv) != 3:
    invalid()
elif not (sys.argv[1] == "-f" or sys.argv[1] == "--font"): #cookin or cooked 🥀🍂💔
    invalid()
else:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        invalid()
    input = input("text: ")
    print(figlet.renderText(input))
