def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye {name}")

# makes code under not get run if sayings.py is imported
if __name__ == "__main__":
    main()