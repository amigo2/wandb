from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


@login_required
def home(request):
    return render(request, 'home.html')
   #return HttpResponse("Hello, world. main index")

