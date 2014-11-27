from django.conf.urls import patterns, url
from backend import views

urlpatterns = patterns('',
	# /backend//1/functions
	#url(r'^functions/$', views.FunctionList.as_view(), name='functions'),
	url(r'^projects/(?P<function_project>\d+)/functions$', views.FunctionList.as_view(), name='function_list'),
	# /backend/1/capabilities
	url(r'^projects/(?P<capability_project>\d+)/capabilities/$', views.CapabilityList.as_view(), name='capability-list'),
	# /backend/capabilities/add - Add capabilities
	url(r'^projects/(?P<capability_project>\d+)/capabilities/add/$', views.Add_Capability.as_view(), name='add-capability'),
	# /functions/1
	url(r'^projects/(?P<pk>\d+)/functions/(?P<function_id>\d+)/$', views.FunctionDetail.as_view(), name='function-detail'),
	# /backend/projects/1/roles
	url(r'^projects/(?P<role_project>\d+)/roles/$', views.RoleList.as_view(), name='roles'),	
	# /backend/projects/1/roles
	url(r'^projects/(?P<resource_project>\d+)/resources/$', views.ResourceList.as_view(), name='resources'),	
	# /backend/projects
	url(r'^projects/$', views.ProjectList.as_view(), name='projects'),	
	# /backend/projects/[proj_name]/
	url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project-detail'),	
)