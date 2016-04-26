__author__ = 'hzliyong'

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']

year = int(input('Year:'))
month = int(input('Month:'))
day = str(input('Day:'))

month_name = months[month - 1]
ordinal = day + endings[int(day) - 1] + ''
print(month_name + ' ' + ordinal + '. ' + str(year))
