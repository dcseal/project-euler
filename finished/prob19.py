# calendar problem
#
# Given that Jan 1, 1900 was a Monday, how many Sundays fell on the first of the
# month during the entire 20th century?

"""
days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', \
    5:'Saturday', 6:'Sunday'}

days_per_month = {}
days_per_month['Jan'] = 31
days_per_month['Feb'] = 28
days_per_month['Mar'] = 31
days_per_month['Apr'] = 30
days_per_month['May'] = 31
days_per_month['Jun'] = 30
days_per_month['Jul'] = 31
days_per_month['Aug'] = 31
days_per_month['Sep'] = 30
days_per_month['Oct'] = 31
days_per_month['Nov'] = 30
days_per_month['Dec'] = 31
"""

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# number of years to count
num_years = 100

# fast forward through first year to figure out days_past_1901
days_past_1900 = 0
if( 1900 % 4 == 0 ):

    # check for a leap year
    if( 1900%4 == 0 ):
        num_days = 366
        days_per_month[1] = 29
    else:
        num_days = 365
        days_per_month[1] = 28
    for m in range( 12 ):
        days_past_1900 += days_per_month[m]

# counters
num_sundays    = 0
days_past_1900 = 0
for n in range(num_years):

    # check for a leap year
    if( n%4 == 0 ):
        num_days = 366
        days_per_month[1] = 29
    else:
        num_days = 365
        days_per_month[1] = 28

    for m in range( 12 ):
        days_past_1900 += days_per_month[m]
        if( days_past_1900 % 7 == 6 ):
            num_sundays += 1
        
print('num_sundays = %d' % num_sundays )
