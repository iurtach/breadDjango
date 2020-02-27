from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name="home"),
	path('about.html',views.about, name="about"),
	path('menu.html',views.menu, name="menu"),
	path('elements.html',views.elements, name="elements"),
	path('contact.html',views.contact, name="contact"),
	path('team.html',views.team, name="team"),
	path('blog_home.html',views.blog_home, name="blog_home"),
	path('blog_single.html',views.blog_single, name="blog_single"),    
]
