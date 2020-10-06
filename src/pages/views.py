from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request)
	return render(request, "home.html", {})


# Create your views here.
def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contact Page</h1>")