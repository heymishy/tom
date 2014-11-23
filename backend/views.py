from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from backend.models import Function, Role, RoletoFunction, Capability, Project
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
		"""return list of functions"""
		#return Function.objects.order_by('id')
		return Function.objects.filter(capability=self.kwargs['pk'])


class CapabilityList(ListView):
	model = Capability
	context_object_name = 'capability_list'

class RoleList(ListView):
	model = Role
	context_object_name = 'role_list'

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

class Add_Capability(CreateView):
	template_name = 'backend/add_capability.html'
	#form_class = Add_Capability_Form
	model = Capability
	fields = ['name', 'description', 'capability_numx']
	#success_url = reverse_lazy('projects')

''' old form view 
def add_capability(request):
	# A HTTP POST?
    if request.method == 'POST':
        form = CapabilityForm(request.POST)

        if form.is_valid():
        	form.save(commit=True)
        	return ProjectDetail(request)
        else:
        	print form.errors
    else:
    	form = CapabilityForm()

    return render(request, 'backend/add_capability.html', {'form': form})
'''
