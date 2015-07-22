# Counting Sundays
# Problem 19

"""
You are given the following information,
but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly
    divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Extra month at the begining to start counting at 1
monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Starting on mondays, wich day is sunday
days = [0, 0, 0, 0, 0, 0, 1]


def main():
    dayCount = 0
    sundays = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            # Reset counter from last month
            daysThisMonth = 0
            # Febraury can have an extre day
            if month == 2:
                if year % 4 == 0 or year % 400 == 0:
                    daysThisMonth = monthDays[month]+1

            daysThisMonth = monthDays[month]

            for day in range(1, daysThisMonth+1):
                # days[currentDay % 7] will return 1 is its sunday, else 0
                # the info is about 1900, but I need to check from 1901
                if day == 1 and (year != 1900):
                    sundays += days[dayCount % 7]

                dayCount += 1

    print sundays


if __name__ == "__main__":
    main()
