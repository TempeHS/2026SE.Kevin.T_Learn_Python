def main():
    tweet = input("Tweet: ")
    print(no_vowels(tweet))

def no_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u"]

    converted = ""
    for letter in sentence:
        if letter not in vowels:
            converted += letter
    return converted

main()