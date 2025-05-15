from datetime import date
import inflect
import sys

inflect = inflect.engine()

class Seasons:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def get(cls):
        while True:
            dob = input("Date of birth (1234-56-78): ")
            try:
                return date.fromisoformat(dob)
            except ValueError:
                print("Invalid date")

def convert(date):
    converted = (date.today() - date).days * 1440
    return inflect.number_to_words(converted, andword="")

def main():
    joe = Seasons.get()
    print(convert(joe))

if __name__ == "__main__":
    main()