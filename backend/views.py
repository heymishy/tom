from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from backend.models import Function, Role, RoletoFunction, Capability
# Create your views here.

class FunctionList(ListView):
	model = Function
	context_object_name = 'function_list'

	def get_queryset(self):
		"""return list of functions"""
		return Function.objects.order_by('id')

class DetailView(DetailView):
	model = Function
	template_name = 'backend/function_detail.html'

class CapabilityList(ListView):
	model = Capability
	context_object_name = 'capability_list'

class RoleList(ListView):
	model = Role
	context_object_name = 'role_list'