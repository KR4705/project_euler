import time
start = time.time()
name_day =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
# leap year
leap_year = []
leap_year.extend(normal_year)
leap_year[1] = 29


def is_leap(year):
	if year % 100 == 0:
		return year/100 % 4 == 0
	else:
		return year % 4 == 0
count = 0 #answer counter
curr_day = 0 #day of the week iterator
for year in range(1900,2001):
	if is_leap(year):
		for current_month in leap_year:
			for day_month in range(current_month):
				if day_month == 0 and curr_day == 6:
					if year > 1900:
						count += 1
				curr_day = (curr_day + 1) % 7
	else :
		for current_month in normal_year:
			for day_month in range(current_month):
				if day_month == 0 and curr_day == 6:
					if year > 1900:
						count += 1
				curr_day = (curr_day + 1) % 7

runtime = time.time() - start
print count , "runtime :%rms" % (runtime*1000)




