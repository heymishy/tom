from django.conf.urls import patterns, url
from backend import views

urlpatterns = patterns('',
	# /backend/functions
	url(r'^functions/$', views.FunctionList.as_view(), name='functions'),
	
	# /functions/1
	url(r'^functions/(?P<function_id>\d+)/$', views.DetailView.as_view, name='function_detail'),
	
	# roles/
	#url(r'^roles/$', views.roles, name='roles'),

	# /backend/functions
	url(r'^capabilities/$', views.CapabilityList.as_view(), name='functions'),

	# /backend/roles
	url(r'^roles/$', views.RoleList.as_view(), name='roles'),	

)