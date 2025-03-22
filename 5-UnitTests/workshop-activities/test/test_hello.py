from hello import hello
# idk why i cnat import hello its probably coz its in a upper folder

def test_default():
    assert hello() == "hello, world"

def test_argumemt():
    assert hello("David") == "hello, David"