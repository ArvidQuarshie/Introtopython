#!usr/bin/python
import datetime
from datetime import timedelta

def gigasecond():
    today=datetime.date.today()
    answer=today+timedelta(1e9)
    print "years:%s"%answer
    
    
    
