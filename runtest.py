import time
import calendar
import datetime

def getVacationDate(year):
	start = str (year) + '-12-21'
	start_day = datetime.datetime.strptime(start, '%Y-%m-%d')
	for i in range(5):
		delta = datetime.timedelta(days=73)
		vacation = start_day + delta*(i+1)
		print(vacation)

getVacationDate(2016)