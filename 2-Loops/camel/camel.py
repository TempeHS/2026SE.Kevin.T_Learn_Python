def main():
    variable = input("Variable: ")
    print(snake_convert(variable))

def snake_convert(camel):
    snake = ""
    for letter in camel:
        if str(letter).isupper() == True:
            converted_letter = "_" + letter.lower()
            snake += converted_letter
        else:
            snake += letter
    return snake
    #need to return something so it doesnt output None at the end
    #may have used ai 💔

main()