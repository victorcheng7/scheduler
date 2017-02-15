from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#add redirect() when i want to redirect a view
def index(request):
    context = {}
    template = "index/index.html"
    return render(request, template, context)
