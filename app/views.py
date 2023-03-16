from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':2,'b':3}
    return render(request,'conditions.html',d)