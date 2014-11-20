from django.contrib import admin
from backend.models import *
# Register your models here.

class Role2FunctionInline(admin.TabularInline):
	model = RoletoFunction
	extra = 2

class RoleAdmin(admin.ModelAdmin):
	inlines =(Role2FunctionInline, )

class FunctionAdmin(admin.ModelAdmin):
	inlines =(Role2FunctionInline, )

class FunctionInline(admin.TabularInline):
	model = Function
	extra = 3


class CapabilityAdmin(admin.ModelAdmin):
	fieldsets = [
		
		(None, 			{'fields': ['name']}),
		('Description', {'fields': ['description'],}),
		('Status',		{'fields': ['status']}),
		('Level', 		{'fields': ['level']}),
		('Domain', 		{'fields': ['domain']}),
		('Project', 	{'fields': ['project']}),
		]
	inlines = [FunctionInline]

admin.site.register(Domain)
admin.site.register(Capability, CapabilityAdmin)
admin.site.register(Function, FunctionAdmin) 
admin.site.register(Role, RoleAdmin)
admin.site.register(Vision)
admin.site.register(Principle)
admin.site.register(Issue)
admin.site.register(Resource)
admin.site.register(Project)
