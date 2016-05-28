from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return HttpResponse ('Hello, world. you are at index pool.')



def search(request):
	data={'name': 'ahmend', 'post': 'SE'}
	return render(request, 'new_1.html',data)

	