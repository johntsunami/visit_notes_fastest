import datetime

# step 1create datetime object
d = datetime.date(1980,3,23)
print(d)

def get_todays_date():
    tday = datetime.date.today()
    print("Todays date is :",tday)
    return tday
# GET DAY OR MONTH OF DATETIME OBJECT OF DATETIME OBJECT
def get_day_mon_or_year():
    print(d.day)  #tday needs to be datetime object
    print(d.year)
    print(d.month)

def get_weekday():
    weekday = d.weekday()
    # mon is 0  sunday is 7 of index

#create timedelta
def add_days(days_to_add): # to see what future date will be, can use this returned variable to subtract from the date as well
    days_added_to_date = datetime.timedelta(days=days_to_add)
    print(days_added_to_date)
    return days_added_to_date  #These return a timedelta
    ## THIS OUTPUT Needs to be subtracted or added to date you want to add/sub

## SEE IF DATE IS BEFORE OR AFTER ANOTHER
 #   USE date1 > date2   #returns boolean

# date = '4/19/2022'
# date = date.split('/')
# month = int(date[0])
# day = int(date[1])
# year = int(date[2])
# print("YEAR:",year)

# new = datetime.date(year,month,day)


