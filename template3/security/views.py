from django.shortcuts import render
from django.http import HttpResponse
from . models import Candidate, Pastcandidate
# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'index.html', context)

def about(request):
    pastcandidates = Pastcandidate.objects.all()
    context = {'pastcandidates':pastcandidates}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')
    