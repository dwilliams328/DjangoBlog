from django.shortcuts import render
from django.http import HttpResponse

def tester(request):
	return render(request,'home.html')