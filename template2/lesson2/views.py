from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_form(request):
    return render(request, 'form.html')

# def contact(request):
#     return render(request, 'contact.html')