# Returns all Tuesdays and Thursdays of a given year
from datetime import datetime as dt
from datetime import date 
import calendar
import requests

def get_thursdays():
    years = [2021]
    c = calendar.TextCalendar(calendar.SUNDAY)
    dates = []
    for year in years:
        for m in range(1,13):
            for i in c.itermonthdays(year,m):
                if i != 0:                                      #calendar constructs months with leading zeros (days belongng to the previous month)
                    day = date(year,m,i)
                    if day.weekday() == 3: #if its Tuesday or Thursday
                        dates.append("%s-%s-%s" % (calendar.month_name[m],i,year))
                    if date(year,m,i) == dt.today().date():
                        return dates

dates = get_thursdays()

prefix = "https://www.mass.gov/doc/weekly-covid-19-municipality-vaccination-report-"
postfix = "/download"
for d in dates:
    url = prefix + d.lower() + postfix
    resp = requests.get(url)
    content_type = resp.headers['Content-Type']
    if content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        with open(d + '.xlsx', 'wb') as r:
            r.write(resp.content)
