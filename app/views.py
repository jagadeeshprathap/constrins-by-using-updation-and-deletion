from django.shortcuts import render

# Create your views here.
from app.models import *

def display(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}

    return render(request,'display.html',context=d)

def display1(request):
    WOT=Webpage.objects.all()
    d={'obj':WOT}

    return render(request,'display1.html',context=d)
def display2(request):
    AOT=AccessRecords.objects.all()
    d={'access':AOT}

    return render(request,'display2.html',context=d)
def display_update(request):
    WOT=Webpage.objects.filter(name='vijji').update(name='AZEEM')
    WOT=Webpage.objects.filter(name='asif').update(url='https//:asif.com')
    WOT=Webpage.objects.all().update(url='https//:jaga.com')
    WOT=Webpage.objects.update_or_create(name='narendra',defaults={'name':'nare'})
    return render(request,'display1.html')
def display_delete(request):
    WOT=Webpage.objects.filter(name='asif').delete()
    WOT=Webpage.objects.all().delete()
    return render(request,'display1.html')