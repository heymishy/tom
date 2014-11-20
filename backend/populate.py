mport os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from backend.models import Domain, Capability, Function, Role, RoletoFunction, Vision, Principle, Proces, Resource, Issue