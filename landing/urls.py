from django.urls import path #import the path from the django to urls
from landing.views import Index

urlpatterns = [
	path('', Index.as_view(), name='index'),
]