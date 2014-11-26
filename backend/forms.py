from django import forms
from backend.models import Function, Role, RoletoFunction, Capability, Project

class FunctionForm(forms.ModelForm):
	name = forms.CharField(max_length=255, help_text="Please enter a name for the function")
	description = forms.CharField(max_length=255, help_text="Please enter a description for the function")
	#status = forms.CharField(widget=forms.HiddenInput(), initial="")
	#capability = forms.ForeignKey(Capability)
	#function_num = forms.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	#project = forms.ManyToManyField(Project, null=True)

	class Meta:
        # Provide an association between the ModelForm and a model
		model = Function
                fields = ('name', 'description',)

class CapabilityForm(forms.ModelForm):
	name = forms.CharField(max_length=255, help_text="Please enter a name for the capability")
	description = forms.CharField(max_length=255, help_text="Please enter a description for the capability")
	#status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	capability_num = forms.DecimalField(max_digits=5, decimal_places=4, help_text="Enter a number")
	#project = models.ManyToManyField(Project, null=True)
	#level = models.CharField(max_length=1, choices=LEVELS_CHOICES, default="Approved")
	#domain = models.ManyToManyField(Domain)

	class Meta:
        # Provide an association between the ModelForm and a model
		model = Capability
                fields = ('name', 'description',)
	def form_valid(self, form):
		proj = form.save(commit=False)
		proj.proj_id = self.kwargs['capability_project']
		proj.save()
		self.object = proj
		return HttpResponseRedirect(self.get_success_url())