from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mobile(request):

    # Page from the theme 
    return render(request, 'pages/mobile.html')