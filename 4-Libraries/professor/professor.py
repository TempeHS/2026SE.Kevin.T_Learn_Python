import random

# Prompts the user for a level,

# If the user does not input 1, 2, or 3, the program should prompt again.

# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative
# integer with n digits. No need to support operations other than addition (+).

# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# the program should output EEE and prompt the user again, allowing the user up to three tries in total for 
# that problem. If the user has still not answered correctly after three tries, the program should output the 
# correct answer.

# The program should ultimately output the user’s score: the number of correct answers out of 10. Structure 
# your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and 
# returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits 
# or raises a ValueError if level is not 1, 2, or 3:


def main():
    level = get_level()
    #print(generate_integer(level))
    #print(make_problem(level))
    solve_problem(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level >= 1 and level <= 3:
            return level


def generate_integer(level):
    return random.randint(10**(level-1), (10**level)-1)
    # black dark doom evil magic code
    # generates number with n amount of digits
    # eg with a level of 3:
    # 10 squared by 3 - 1 (2) = 100
    # 10 squared by 3 = 1000 - 1 = 999

def make_problem(level):
    return str(generate_integer(level)) + " + " + str(generate_integer(level))

def solve_problem(level):
    correct_questions = 0
    for i in range(10):
        problem = make_problem(level)
        print(f"Solve: {problem}")
        
        tries = 3
        while tries > 0:
            try:
                solution = int(input("Solution: "))
            except ValueError:
                continue
            # so if i knew eval existed before then it would all be good and well
            if solution == eval(problem):
                print("Correct!")
                print()
                correct_questions += 1
                break
            else:
                print("EEE")
                print(f"Solve: {problem}")
                print()
                tries -= 1
                continue
        if tries <= 0:
            print(f"Solution: {problem} = {str(eval(problem))}")
    print(correct_questions)

if __name__ == "__main__":
    main()