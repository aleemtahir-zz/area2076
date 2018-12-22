from django.urls import path
from django.conf.urls import url
from area2076 import views

urlpatterns = [
	# url(r'^$', views.index, name='index')
	path('', views.index, name='main-view'),
	path('profile/', views.profile, name='profile-view'),
	# path('examples/', views.examples, name='examples'),
	# path('contact/', views.contact, name='contact'),
]