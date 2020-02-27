from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def elements(request):
	return render(request, 'elements.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def menu(request):
	return render(request, 'menu.html', {})

def blog_home(request):
	return render(request, 'blog_home.html', {})

def blog_single(request):
	return render(request, 'blog_single.html', {})

def team(request):
	return render(request, 'team.html', {})
# Create your views here.
