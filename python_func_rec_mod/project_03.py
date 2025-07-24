# project : The calender app 

import calendar
def show_calender():
    year=int(input("enter the year:"))
    month=int(input("enter the month(1-12) :"))
    print("\ncalender : ")
    print(calendar.month(year,month))
show_calender()
