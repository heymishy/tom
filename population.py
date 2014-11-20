import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tom.settings')

import django
django.setup()

from backend.models import Domain, Capability, Function, Role, RoletoFunction, Vision, Principle, Proces, Resource, Issue

def populate():
	code_cap = add_cat('Manage Code')
    domain = "Software Development"

    add_func(cat=code_cap,
        domain=domain,
        name="Create design specification",
        )

def add_func(cap, domain, name):
    f = Function.objects.get_or_create(capability=cap, name=name, description=desc, status="Approved", domain=domain)[0]
    return p

def add_cap(name):
    c = Capability.objects.get_or_create(name=name, status="Approved", project="Product Reporting")[0]
    return c

def add_domain(name):
    d = Domain.objects.get_or_create(name=name)[0]
    return c

def add_project(name):
    p = Project.objects.get_or_create(name=name)[0]
    return p

# Print out what we have added to the user.
    for c in Capability.objects.all():
        for p in Function.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

# Start execution here!
if __name__ == '__main__':
    print "Starting TOM population script..."
    populate()


"1","Product Development"
"2","Business Development"
"5","Service Fund"
"6","Service Client"
"0.2","Report AUM"
"1.1","Develop Product / Client Solutions"
"1.2","Market Product"
"2.1","Pitch to Client / Prospect"
"2.2","Manage Consultant Relationship"
"3.1","Define & Agree Terms"
"6.1","Review Client"
"6.2","Produce Client Reports"
"3.2","Transition Segregated Client"
"1.3","Manage Investment Pipeline"
"4","Invest Money"
"4.1","Understand Investment Process"
"5.1","Produce Fund Reports"
"7.1","Manage Product Team"
"3","Take On Client"
"2.3","Complete RFPs"
"0.1","Manage Data"
"2.1.1","Pitch to new opportunity"
"2.1.2","Request material to support pitch"
"2.1.3","Discuss pricing"
"2.1.4","Develop proposal materials"
"3.1.1","Set pricing"
"3.1.2","Sign off IMA"
"1.2.1","Produce sales aids"
"1.2.2","Review sales aids"
"1.2.3","Prepare material for conferences"
"1.2.4","Present at conferences"
"1.2.5","Produce other marketing materials (MA only)"
"1.2.6","Produce think pieces (MA only)"
"2.2.2","Consultant questionnaires"
"2.2.1","Consultant DB update"
"2.3.1","Maintain Std. RFP"
"2.3.2","Complete RFP"
"2.3.3","DDQs"
"2.3.4","Maintain QVIDIAN"
"2.3.5","Sign off RFPs"
"5.1.1","Produce factsheet"
"5.1.2","Produce Fund Update"
"5.1.3","Produce Newsletter"
"5.1.4","Produce KIID"
"5.1.5","Produce Strategy Factsheet"
"5.1.6","Produce flash reports"
"5.2","Review Fund Reports"
"5.2.1","Review factsheet"
"5.2.2","Review Fund Update"
"5.2.3","Review Newsletter"
"5.2.4","Review KIID"
"5.2.5","Review Strategy Factsheet"
"5.2.6","Review flash reports"
"4.1.1","Create content to describe Investment Process"
"0.1.1","Extract data"
"0.1.2","Manipulate data"
"0.1.3","Maintain Bios"
"0.1.4","Maintain staff details"
"6.2.1","Mthly / Qtrly Bespoke"
"6.2.2","Newsletters"
"6.2.3","MIR / QIRS"
"6.2.4","Ad-hoc requests"
"6.2.5","Weekly reporting"
"6.1.1","Prepare material for client review presentations"
"6.1.2","Present client review"
"7.1.1","Training new starters"
"7.1.2","Manage workload"
"0.2.1","Extract AUM"
"0.2.2","Manipulate AUM"
"4.2","Monitor Performance & Attribution"
"4.2.1","Produce performance"
"4.2.2","Produce attribution"
"4.2.3","Manipulate report format"
"0","Data Management"
"2","Business Management"
"1.1.1","Discuss opportunities"
"1.1.2","Research market opportunities"
"1.1.3","Qualify ideas (Product Lab – MA only)"
"3.2.1","Client data review"
"3.2.2","Client report template setup"
"6.3","Manage Report Repository"
"6.3.1","Manage report repository"
"1.3.1","Monitor internal pipeline (MA only)"
"7.2","Supporting Investment Business"
"7.2.1","Produce GMC reports"
"7.2.2","Produce board papers"
"7.2.3","Produce senior mgmt presentations"