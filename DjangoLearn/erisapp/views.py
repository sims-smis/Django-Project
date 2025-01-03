from django.shortcuts import render
from .models import chaiVariety

# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'erisapp/all_chai.html',{chais: 'chais'})