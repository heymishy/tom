Target Operating Model (TOM) Platform
===
Target Operating Model (TOM) Platform

First attempt at building a platform for defining business strategy, solving complex problems or simply providing proper context of the problem being solved.

#Longer term vision# 

Change the way software is designed and communicated

From idea/problem to working solution, complete with constant feedback at every step!

#Installation#

Either use a *nix platform or VM, or adapt these instructions for building a djnango project on Windows

Install python

Download the get-pip script from https://bootstrap.pypa.io/get-pip.py

Run the script

`python get-pip.py

Then install virtualenv

`pip install virtualenv

Make a directory for the project

```
mkdir ~/dev/newproject
cd ~/dev/newproject/
```
make a new virtualenv envrionment
`virtualenv dev-envname

then everytime you want to activate (enter) the environment use the following:
`source ~/dev/newproject/bin/activate

this should then change your command prompt to prefix with 'newproject' to confirm it activated properly
within your environment then install django

`pip install django

clone the repository from github

`git clone https://github.com/heymishy/tom.git

and then run the server 

`python manage.py runserver