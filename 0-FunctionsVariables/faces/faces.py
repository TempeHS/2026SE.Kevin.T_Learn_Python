def convert(str):
    str2 = str.replace(":)","🙂")
    return str2.replace(":(","🙁")

def main():
    sentence = input("Input: ")
    print(convert(sentence))

main()
