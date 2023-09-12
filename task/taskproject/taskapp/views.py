from django.http import HttpResponse
from django.shortcuts import render
from . models import orders


# Create your views here.
def index(request):
    c = orders.objects.all()
    return render(request,'index.html',{'obj':c})
