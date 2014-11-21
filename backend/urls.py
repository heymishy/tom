from django.conf.urls import patterns, url
from backend import views

urlpatterns = patterns('',
	# /backend/functions
	url(r'^functions/$', views.FunctionList.as_view(), name='functions'),
	# /backend/capabilities
	url(r'^capabilities/$', views.CapabilityList.as_view(), name='functions'),
	# /backend/add_capability - Add capabilities
	url(r'^add_capability/$', views.add_capability, name='add_capability'),
	# /functions/1
	url(r'^functions/(?P<pk>\d+)/$', views.DetailView.as_view, name='function_detail'),
	# /backend/roles
	url(r'^roles/$', views.RoleList.as_view(), name='roles'),	
	# /backend/projects
	url(r'^projects/$', views.ProjectList.as_view(), name='projects'),	
	# /backend/projects/[proj_name]/
	url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project_detail'),	
)