from datetime import date, timedelta
import datetime as dt

def gigasecond_date(date):
    date=raw_input("Enter date")
    return str(date)+timedelta(0,10**9)


Next=gigasecond_date(12/12/12)

print "the year will be %s" %Next

print "the day will be %s" %Next.strftime("%m/%d%y")
