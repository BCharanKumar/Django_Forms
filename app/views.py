from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def studentdjf(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            #return HttpResponse(SFDO)
            #return HttpResponse(str(SFDO))
            return HttpResponse(str(SFDO.cleaned_data))
            #return HttpResponse(str(SFDO.cleaned_data['sname']))

        
        else:
            return HttpResponse('Invalid Details')
    return render(request,'studentdjf.html',d)