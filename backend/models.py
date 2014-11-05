from django.db import models

# Create your models here.
class Domain(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	
	def __str__(self):              # __unicode__ on Python 2
	    return self.name	

class Capability(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)

	LEVELS_CHOICES = (
		('0', 'Level 0'),
		('1', 'Level 1'),
		('2', 'Level 2'),
		('3', 'Level 3'),
		)

	level = models.CharField(max_length=1, choices=LEVELS_CHOICES)
	
	domain = models.ManyToManyField(Domain)

	def __str__(self):              # __unicode__ on Python 2
	    return self.name


class Function(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	capability = models.ForeignKey(Capability)
	def __str__(self):              # __unicode__ on Python 2
	    return self.name

class Role(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	performs_func = models.ManyToManyField(Function, through='RoletoFunction')
	def __str__(self):              # __unicode__ on Python 2
	    return self.name

class RoletoFunction(models.Model):
	role = models.ForeignKey(Role)
	function = models.ForeignKey(Function)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	allocation = models.IntegerField()
	def __str__(self):  
	    return self.name	

class Vision(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	owner = models.CharField(max_length=255)
	def __str__(self):              # __unicode__ on Python 2
	    return self.name

class Principle(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	def __str__(self):              # __unicode__ on Python 2
	    return self.name

class Proces(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	def __str__(self):              # __unicode__ on Python 2
	    return self.name

class Resource(models.Model):
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	def __str__(self):              # __unicode__ on Python 2
	    return self.name

class Issue(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	def __str__(self):              # __unicode__ on Python 2
	    return self.name