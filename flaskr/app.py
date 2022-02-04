import mimetypes
from flaskr import app
from flask import request,render_template,redirect,url_for




@app.route('/')
def get_file():   
    return render_template('file.html')



def descOrder(lists):
    lists.reverse()
    str1 = ''.join(lists)
    return str1

@app.route('/download')
def download():
    date=request.args.get('date').strip() 
    lists=list(date)
    order=descOrder(lists)
   
    month=list(order[3:5])
    day=list(order[0:2])
    year=list(order[6:10])
    ordered_day=descOrder(day)
    ordered_year=descOrder(year)
    ordered_month=descOrder(month)
    
   

    return render_template('download.html',day=ordered_day,month=ordered_month,year=ordered_year)





