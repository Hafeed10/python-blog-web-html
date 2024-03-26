from django.shortcuts import render
from django.http.response import HttpResponse

def index (request):
    context = {
        "title":"HomePage"
    }
    return render(request ,'web/end.html', context=context)
