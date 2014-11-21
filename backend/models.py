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
	
	def __str__(self): 
	    return self.proj_name	

class Domain(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	domain_num = models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)
	project = models.ManyToManyField(Project, null=True)
	
	def __str__(self): 
	    return self.name	

class Capability(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	capability_num = models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)
	project = models.ManyToManyField(Project, null=True)

	LEVELS_CHOICES = (
		('0', 'Level 0'),
		('1', 'Level 1'),
		('2', 'Level 2'),
		('3', 'Level 3'),
		)

	level = models.CharField(max_length=1, choices=LEVELS_CHOICES, default="Approved")
	domain = models.ManyToManyField(Domain)

	class Meta:
		verbose_name_plural = "Capabilities"
	
	def __str__(self):
	    return self.name


class Function(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, default="Approved")
	capability = models.ForeignKey(Capability)
	function_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	project = models.ManyToManyField(Project, null=True)
	
	def __str__(self):  
	    return self.name

class Role(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	performs_func = models.ManyToManyField(Function, through='RoletoFunction')
	role_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)

	def __str__(self):  
	    return self.name

class RoletoFunction(models.Model):
	role = models.ForeignKey(Role)
	function = models.ForeignKey(Function)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	allocation = models.DecimalField(max_digits=5, decimal_places=2)
	roletofunction_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)

	def __str__(self):  
	    return self.name	

class Vision(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	owner = models.CharField(max_length=255)
	vision_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	project = models.ManyToManyField(Project, null=True)

	def __str__(self):
	    return self.name

class Principle(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	principle_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	project = models.ManyToManyField(Project, null=True)

	def __str__(self):
	    return self.name

class Proces(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	process_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
	project = models.ManyToManyField(Project, null=True)

	class Meta:
		verbose_name_plural = "Processes"

	def __str__(self):
	    return self.name

class Resource(models.Model):
	resource_name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	resource_num = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)

	def __str__(self):
	    return self.name

class Issue(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Approved")
	issue_num = models.DecimalField(max_digits=5, decimal_places=4, null=True)
	project = models.ManyToManyField(Project, null=True)

	def __str__(self):
	    return self.name