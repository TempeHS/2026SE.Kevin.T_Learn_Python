import emoji

input = input("Emoji: ")
emojized = emoji.emojize(input, language="alias")
print("Output:", emojized)