from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
# Create your views here.



def index(request):
    card = Card.objects.all()
    return render(request,"base.html" , {'card':card})
