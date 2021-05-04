''' Programme to find leap year with the between range 1900 and 10 pow 5'''

def is_leap(year):
    leap = False
    year = int(year)
    # Write your logic here
    print(year)
    if (year >= 1900 and year <= 10**5):
        print(year % 400 , year % 100 != 0 ,year % 4)
        if( (year % 4 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
            print(year ," is a leap year")
            leap = True
        else:
            print("inside if but in else")
    else:
        print("outside if but in else")

    return leap


#year = input("enter a year")
while True:
    year = input("enter a year: ")
    print(is_leap(year))