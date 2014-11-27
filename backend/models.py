from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


STATUS_CHOICES = (
		('Approved', 'Approved'),
		('Draft', 'Draft'),
		('Retired', 'Retired'),
		)

class Project(models.Model):
	proj_name = models.CharField(max_length=255, null=True, blank=True)
	description = models.CharField(max_length=255, null=True, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	project_num = models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)
	created_by = models.ForeignKey(User, default=0, related_name='created_by')
	assigned_to = models.ManyToManyField(User, default=0, related_name='assigned_to')
	def __str__(self): 
	    return self.proj_name	

class Domain(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	domain_num = models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)
	project = models.ManyToManyField(Project, null=True)
	created_by = models.ForeignKey(User, default=0)

	def __str__(self): 
	    return self.name	

class Capability(models.Model):
	name = models.CharField(max_length=255, help_text="Name")
	description = models.CharField(max_length=255, blank=True, help_text="Description")
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved", help_text="Status")
	capability_num = models.DecimalField(max_digits=5, decimal_places=2, help_text="Number")
	project = models.ManyToManyField(Project, null=True, help_text="Project")

	LEVELS_CHOICES = (
		('0', 'Level 0'),
		('1', 'Level 1'),
		('2', 'Level 2'),
		('3', 'Level 3'),
		)

	level = models.CharField(max_length=1, choices=LEVELS_CHOICES, help_text="Level")
	domain = models.ManyToManyField(Domain, help_text="Domain")
	created_by = models.ForeignKey(User, default=0, help_text="Created by")

	class Meta:
		verbose_name_plural = "Capabilities"
        ordering = ['id']
	
	def __str__(self):
	    return self.name
	
	def get_absolute_url(self):
		return reverse('project_detail', kwargs={'pk': self.pk})


class Function(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, default="Approved")
	capability = models.ForeignKey(Capability)
	function_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	performs_role = models.ManyToManyField('Role', through='RoletoFunction', blank=True, null=True)
	#project = models.ManyToManyField(Project, null=True)
	created_by = models.ForeignKey(User, default=0)

	def __str__(self):  
	    return self.name

class Role(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	performs_func = models.ManyToManyField(Function, through='RoletoFunction', blank=True, null=True)
	role_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	created_by = models.ForeignKey(User, default=0)
	project = models.ManyToManyField(Project, null=True, blank=True)
	
	def __str__(self):  
	    return self.name

class RoletoFunction(models.Model):
	role = models.ForeignKey(Role,blank=True, null=True)
	function = models.ForeignKey(Function, blank=True, null=True)
	name = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	allocation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	roletofunction_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	created_by = models.ForeignKey(User, default=0, blank=True, null=True)
	def __str__(self):  
	    return self.name	

class Vision(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	owner = models.CharField(max_length=255)
	vision_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	#project = models.ManyToManyField(Project, null=True)
	created_by = models.ForeignKey(User, default=0)

	def __str__(self):
	    return self.name

class Principle(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	principle_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	project = models.ManyToManyField(Project, null=True)
	created_by = models.ForeignKey(User, default=0)

	def __str__(self):
	    return self.name

class Proces(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	process_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	project = models.ManyToManyField(Project, null=True)
	created_by = models.ForeignKey(User, default=0)

	class Meta:
		verbose_name_plural = "Processes"

	def __str__(self):
	    return self.name

class Resource(models.Model):
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	resource_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	created_by = models.ForeignKey(User, default=0)
	project = models.ManyToManyField(Project, null=True)
	role = models.ManyToManyField(Role, null=True, blank=True)

	def __str__(self):
	    return self.name

class Issue(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	issue_num = models.DecimalField(max_digits=5, decimal_places=4, null=True)
	project = models.ManyToManyField(Project, null=True)
	created_by = models.ForeignKey(User, default=0)

	def __str__(self):
	    return self.name