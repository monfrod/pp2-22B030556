from datetime import date, timedelta
dyesterday = date.today() - timedelta(1)
dtomorrow = date.today() + timedelta(1)
print ('Yesterday: ',dyesterday)
print('Today :',date.today())
print('Tomorrow: ',dtomorrow)
