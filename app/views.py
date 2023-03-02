from django.shortcuts import render

# Create your views here.
import datetime

def filter(request):
    t=datetime.datetime.now()
    d={'data':'hi HOW are u all','t':t,'c':10}
    return render(request,'filter.html',d)