from django.shortcuts import render
from .models import Kerdes
import random

def index(request):
    template = "index.html"
    r = random.randrange(len(Kerdes.objects.all))
    alany = Kerdes.objects.filter(hanyadik = r).first()
    context = {'kerdes' : alany}
    return render(request, template, context)