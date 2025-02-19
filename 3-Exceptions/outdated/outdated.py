def main():
    date = input("Date: ")
    new_date = convert_date(date)
    print(new_date)

def convert_date(old_date):
    # old date = mm/dd/yyyy or month day, year
    # this is for mm/dd/yyyy
    if "/" in old_date:
        split_date = old_date.split("/")
        day = 
        # turns it into year month day
        return f"{split_date[2]}-{split_date[0]}-{split_date[1]}"

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


main()