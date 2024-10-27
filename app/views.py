from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
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


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=request.POST['tn']
            TO=Topic.objects.create(topic_name=tn)

            return HttpResponse('Topic object created Successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={"EWFO":EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            topic_name=request.POST['topic_name']
            TO=Topic.objects.get(topic_name=topic_name)
            name=request.POST['name']
            url=request.POST['url']
            email=request.POST['email']
            WO=WebPage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
            return HttpResponse('webpage object created Successfully')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_webpage.html',d)


def inser_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}

    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST) 
        if AFDO.is_valid():
            name=request.POST['name']
            WO=WebPage.objects.get(id=name)
            author=request.POST['author']
            date=request.POST['date']
            AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)
            return HttpResponse('Access Record object created Successfully')
        else:
            return HttpResponse('invalid data here...!  ')

    return render(request,'inser_accessrecord.html',d)