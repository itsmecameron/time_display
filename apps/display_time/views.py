from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import datetime

def index(request):
    current_date_time = datetime.datetime.now()

    context = {
        "datetime": strftime("%d-%b-%Y %H:%M %p", gmtime()),
        'day': current_date_time.day,
        'month': current_date_time.strftime('%b'),
        'year': current_date_time.year,
        'time': current_date_time.strftime('%I:%M %p '),
    }
    return render(request,"display_time/index.html", context)