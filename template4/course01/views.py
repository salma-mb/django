from django.shortcuts import render
from django.http import HttpResponse
from . models import Candidate
# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'index.html', context)

def view_form(request):
    return render(request, 'form.html')

def contact(request):
    return render(request, 'contact.html')