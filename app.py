from flask import flash, request,render_template,redirect,url_for,Flask
from datetime import date, timedelta, datetime
import calendar
import requests
from bs4 import BeautifulSoup
import pytz
app=Flask(__name__)
app.config['SECRET_KEY']="naut1234567"


def descOrder(lists):
    for r in lists:      
        r.reverse()
    return r
def descSearch(lists):
    lists.reverse()
    str1=''.join(lists)
    return str1


 
local_tz = pytz.timezone('Africa/Lagos') 
local=datetime.now(local_tz)      

@app.route('/search')
def search():
    date=request.args.get('date').strip() 
    lists=list(date)
    order=descSearch(lists)  
    month=list(order[3:5])
    day=list(order[0:2])
    year=list(order[6:10])
    
    ordered_day=descSearch(day)
    ordered_year=descSearch(year)
    ordered_month=descSearch(month)
    now=local
    month_name=calendar.month_name[now.month]
    if int(ordered_day) > now.day or int(ordered_month) > now.month or int(ordered_year) > now.year:
       flash('Date can not be greater than present date','danger')
       return redirect(url_for('naut_files')) 
    return render_template('search.html',day=ordered_day,month=ordered_month,year=ordered_year,month_name=month_name,now=now)


    
   


@app.route('/')
def naut_files():
    month = local.month
    year = local.year
    current_date=local.day
    # number_of_days = calendar.monthrange(year, month)[1]
    first_date = date(year, month, 1)
    last_date = date(year, month, current_date)
    delta = last_date - first_date
    a=[(first_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
    list=[]
    list.append(a)
    order=descOrder(list)
    now=local
    month_name=calendar.month_name[now.month]

    
    return render_template('pod.html',order=order,now=now,month=month,month_name=month_name)



# Web URL
web_url = "https://polkashots.io/"

# get HTML content
html = requests.get(web_url).content

# parse HTML Content
soup = BeautifulSoup(html, "html.parser")

js_files = []
cs_files = []

for script in soup.find_all("script"):
	if script.attrs.get("src"):
		
		# if the tag has the attribute
		# 'src'
		url = script.attrs.get("src")
		js_files.append(web_url+url)


for css in soup.find_all("link"):
	if css.attrs.get("href"):
		
		# if the link tag has the 'href'
		# attribute
		_url = css.attrs.get("href")
		cs_files.append(web_url+_url)

# adding links to the txt files
with open("javajavascript_files.txt", "w") as f:
	for js_file in js_files:
		print(js_file, file=f)

with open("css_files.txt", "w") as f:
	for css_file in cs_files:
		print(css_file, file=f)
