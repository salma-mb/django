from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view(request):
    return render(request, 'form.html')
def index(request):
    return render(request, 'index.html')