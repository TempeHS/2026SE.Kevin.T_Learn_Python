def convert(str):
    return str.replace(":)","🙂").replace(":(","🙁")

def main():
    sentence = input("Input: ")
    print(convert(sentence))

main()
