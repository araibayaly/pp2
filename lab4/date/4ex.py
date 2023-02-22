from datetime import datetime 

def dif(d1,d2):
    x=d2-d1
    return x.days * 24 * 3600 + x.seconds

date1=datetime.strptime('2021-09-07 01:45:56', '%Y-%m-%d %H:%M:%S')
date2=datetime.now()
print("\n%d seconds" %(dif(date1, date2)))
