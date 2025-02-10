def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# “All vanity plates must start with at least two letters.” (if var was variable then var[0:2] would be va)
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an 
# acceptable vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def is_valid(s):
    return all([
        starts_with_letters(s),
        min_max_characters(s),
        #ends_with_numbers(s)
        ])

# checks below this line
def starts_with_letters(string):
    # [0:2] splits it into the first 2 letters only
    if string[0:2].isalpha():
        print("starts_with_letters = true")

        return True
    
    else:
        print("starts_with_letters = false")

def min_max_characters(string):
    if len(string) >= 2 and len(string) <= 6:
        print("min_max_characters = true")

        return True
    
    else:
        print("min_max_characters = false")

#def ends_with_numbers(string):

# checks above this line

main()

