def convert(time):
	hours = float(time.split(":")[0])
	minutes = float(time.split(":")[1]) / 60
	return hours + minutes

def main():
    usertime = input("What's the time? ")
    if convert(usertime) <= 8 and convert(usertime) >= 7:
        print("breakfast time")
    elif convert(usertime) <= 13 and convert(usertime) >= 12:
        print("lunch time")
    elif convert(usertime) <= 19 and convert(usertime) >= 18:
        print("dinner time")
    else:
        print("nothing")

if __name__ == "__main__":
    main()