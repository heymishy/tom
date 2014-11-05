from django.shortcuts import render
from django.http import Http404

from backend.models import Function
# Create your views here.



def detail(request, function_id):
	try:
		function = Function.objects.get(pk=function_id)
	except Function.DoesNotExist:
		raise Http404
	return render(request, 'backend/detail.html', {'function': function})

def index(request):
	function_list = Function.objects.order_by('id')
	context = {'function_list': function_list}
	return render(request, 'backend/index.html', context)