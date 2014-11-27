from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from backend.models import Function, Role, RoletoFunction, Capability, Project, Resource
from backend.forms import FunctionForm, CapabilityForm

class FunctionList(ListView):
	model = Function
	context_object_name = 'function_list'

	def get_queryset(self):
		"""return list of functions"""
		return Function.objects.order_by('id')

class FunctionDetail(DetailView):
	model = Function
	template_name = 'backend/function_detail.html'
	context_object_name = 'function'
	def get_queryset(self):
	#	"""return list of functions"""
		#self.function = get_object_or_404(Function, name=self.args[0])
		#return Function.objects.filter(id=self.function)
		return Function.objects.order_by('id')
		#return Function.objects.filter(id=self.request.GET.get('id'))
	def get_context_data(self, **kwargs):
		context = super(FunctionDetail, self).get_context_data(**kwargs)
		_id = 0
		if 'function_id' in kwargs:  #this is how you can get function_id's data from url
			_id = int(kwargs['function_id'] or '0')
		function =  Function.objects.get(id=_id)
		context['role_function'] = RoletoFunction.objects.filter(function=function)
		return context

class CapabilityList(ListView):
	model = Capability
	context_object_name = 'capability_list'

	def get_queryset(self):
		self.project = self.kwargs.get("capability_project", None)
		return Capability.objects.filter(project=self.project)

class CapabilityDetail(ListView):
	model = Capability
	context_object_name = 'capability_detail'


class RoleList(ListView):
	model = Role
	context_object_name = 'role_list'
	def get_queryset(self):
		self.project = self.kwargs.get("role_project")
		return Role.objects.filter(project=self.project)

class ProjectList(ListView):
	model = Project
	context_object_name = 'proj_list'

	def get_queryset(self):
		user = self.request.user
		"""return list of functions"""
		return Project.objects.filter(assigned_to=user)

class ProjectDetail(DetailView):
	model = Project
	template_name = 'backend/project_detail.html'

	def get_queryset(self):
		return Project.objects.order_by('id')

class ResourceList(ListView):
	model = Resource
	context_object_name = 'resource_list'
	template_name = 'backend/resource_list.html'

	def get_queryset(self):
		self.project = self.kwargs.get("resource_project", None)
		return Resource.objects.filter(project=self.project)

class Add_Capability(CreateView):
	template_name = 'backend/add_capability.html'
	#form_class = Add_Capability_Form
	model = Capability
	fields = ['name', 'description', 'status', 'capability_num', 'project', 'domain']
	#success_url = reverse_lazy('projects')
