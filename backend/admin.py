from django.contrib import admin
from backend.models import *
# Register your models here.

class CapabilityAdmin(admin.ModelAdmin):
	fieldsets = [
		
		(None, 			{'fields': ['name']}),
		('Description', {'fields': ['description'], 'classes': ['collapse']}),
		('Status',		{'fields': ['status']}),
		('Level', 		{'fields': ['level']}),
		('Domain', 		{'fields': ['domain']}),
		]
admin.site.register(Domain)
admin.site.register(Capability, CapabilityAdmin)
admin.site.register(Function) 
admin.site.register(Role)
admin.site.register(Vision)
admin.site.register(Principle)
admin.site.register(Issue)
admin.site.register(Resource)
