def main():
    tweet = input("Tweet: ")
    print(shorten(tweet))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    converted = ""
    for letter in word:
        if letter not in vowels:
            converted += letter
    return converted


if __name__ == "__main__":
    main()