from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def count(request):
    if 'count' in request.session:
        request.session['count'] += 1

    else: request.session['count'] =1

    unique_id = get_random_string(length=32)

    context = {
        'random': unique_id 
    }

    return render(request,"random_word/index.html", context)

def clear(request):
    if 'count' in request.session:
        del request.session['count']
    return redirect("/random_word")




