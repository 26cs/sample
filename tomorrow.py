import datetime

while True:
    try:
        dd = int(input('Enter date number: '))
        mm = int(input('Enter month number: '))
        yyyy = int(input('Enter year number: '))
        entered_date = datetime.date(year=yyyy, month=mm, day=dd)
        next_date = entered_date + datetime.timedelta(days=1)
        print('Tomorrow is {}/{}/{}'.format(next_date.month, next_date.day, next_date.year))
    except:
        print('You entered wrong value.')

# Result:
# Enter date number: 24
# Enter month number: 07
# Enter year number: 2022
# Tomorrow is 7/25/2022
# Enter date number:
