"""Season"""

def main():
    """Season"""
    month = int(input())
    day = int(input())
    season = ""

    if month in [1, 2 , 3]:
        if month == 3 and day >= 21:
            season = "spring"
        else:
            season = "winter"
    elif month in [4, 5 , 6]:
        if month == 6 and day >= 21:
            season = "summer"
        else:
            season = "spring"
    elif month in [7, 8 , 9]:
        if month == 9 and day >= 21:
            season = "fall"
        else:
            season = "summer"
    elif month in [10, 11 , 12]:
        if month == 12 and day >= 21:
            season = "winter"
        else:
            season = "fall"

    print(season)
main()
