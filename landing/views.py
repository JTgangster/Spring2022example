from django.shortcuts import render
from django.views import View #get and post methods on view class

class Index(View):#different methods on our class for each http method we need to handle
	def get(self, request, *args, **kwargs):#Will run when a get request is sent to this url
		return render(request, 'landing/index.html')#Return a template