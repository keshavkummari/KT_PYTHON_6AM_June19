
#-----------------------------------------------------------#
Web Framework :
#-----------------------------------------------------------#

1. Django
2. Flask
3. Disel

#-----------------------------------------------------------#
Django : Web Applications / WebSites :
#-----------------------------------------------------------#
1. Django is a WebFramework and it is writen in Python

2. A Web Framework is a software that supports the developement of Dynamic WebSites, Applciations, and Services.

3. Web Framework Functionalities :
	1. Security Features
	2. Database Access
	3. Sessions
	4. Template Processing
	5. URL Routing
	6. Internationalization
	7. Localization and Much more.....

4. Web Framework such a Django, enables us to develop secure and reliable Web Applications very quickly in a standardized way,
without having to reinvent the wheel.

#-----------------------------------------------------------#
Who's Using Django?
#-----------------------------------------------------------#

1. Instagram
2. Disqus
3. Mozilla
4. Bitbucket
5. Last.fm
6. National Geographic

#-----------------------------------------------------------#
Download, Install & Configure Django on Operating Systems :
#-----------------------------------------------------------#

1. Windows
2. MacOS
3. Linux
4. Unix

#-----------------------------------------------------------#
On-Premises : Desktop, Laptop & Server HardWare, & Virtualization

Cloud : AWS or AZURE or GCP
#-----------------------------------------------------------#
# python --version

# pip --version

# pip install django

# django-admin --version
#-----------------------------------------------------------#


Step-1 : Check the Version:

$ python -m django --version
1.11.5

Step-2 : Create a Django Project:

$ django-admin startproject kkummari

Step-3 : Check the Project info:

$ ls -ld kkummari/
drwxr-xr-x  4 keshavkummari  staff  128 Nov 12 23:51 kkummari/

$ ls -lrta kkummari/

drwxrwxrwx+ 108 keshavkummari  staff  3456 Nov 12 23:51 ..
-rwxr-xr-x    1 keshavkummari  staff   806 Nov 12 23:51 manage.py
drwxr-xr-x    4 keshavkummari  staff   128 Nov 12 23:51 .
drwxr-xr-x    6 keshavkummari  staff   192 Nov 12 23:51 kkummari

$ ls -lrta kkummari/kkummari/

drwxr-xr-x  4 keshavkummari  staff   128 Nov 12 23:51 ..
-rw-r--r--  1 keshavkummari  staff     0 Nov 12 23:51 __init__.py
-rw-r--r--  1 keshavkummari  staff   765 Nov 12 23:51 urls.py
-rw-r--r--  1 keshavkummari  staff   394 Nov 12 23:51 wsgi.py
drwxr-xr-x  6 keshavkummari  staff   192 Nov 12 23:51 .
-rw-r--r--  1 keshavkummari  staff  3102 Nov 12 23:51 settings.py

These files are:

1. The outer kkummari/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

2. manage.py: A command-line utility that lets you interact with this Django project in various ways.
You can read all the details about manage.py in django-admin and manage.py.

3. The inner kkummari/ directory is the actual Python package for your project.
Its name is the Python package name you’ll need to use to import anything inside it (e.g. kkummari.urls).

4. kkummari/__init__.py: An empty file that tells Python that this directory should be considered a Python package.

5. kkummari/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

6. kkummari/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
You can read more about URLs in URL dispatcher.

7. kkummari/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.


Step-4 : Run The development server :

$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

November 12, 2018 - 18:35:46
Django version 1.11.5, using settings 'kkummari.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


Step-5 : Go to Browser and Cross check the status of the Django project i.e. kkummari

http://127.0.0.1:8000/


Step-6 : Apply Migrations :

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK


Step-7 : Changing the port :

By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

$ python manage.py runserver 8080

$ python manage.py runserver 0:8000


Step-8 : Creating the app

$ python manage.py startapp home

$ ls -lrta
drwxrwxrwx+ 108 keshavkummari  staff    3456 Nov 12 23:51 ..
-rwxr-xr-x    1 keshavkummari  staff     806 Nov 12 23:51 manage.py
drwxr-xr-x    7 keshavkummari  staff     224 Nov 13 00:05 kkummari
-rw-r--r--    1 keshavkummari  staff  131072 Nov 13 00:08 db.sqlite3
drwxr-xr-x    6 keshavkummari  staff     192 Nov 13 00:13 .
drwxr-xr-x    9 keshavkummari  staff     288 Nov 13 00:13 home

$ ls -lrta home/
drwxr-xr-x  6 keshavkummari  staff  192 Nov 13 00:13 ..
-rw-r--r--  1 keshavkummari  staff    0 Nov 13 00:13 __init__.py
-rw-r--r--  1 keshavkummari  staff   63 Nov 13 00:13 views.py
-rw-r--r--  1 keshavkummari  staff   63 Nov 13 00:13 admin.py
-rw-r--r--  1 keshavkummari  staff   83 Nov 13 00:13 apps.py
-rw-r--r--  1 keshavkummari  staff   57 Nov 13 00:13 models.py
-rw-r--r--  1 keshavkummari  staff   60 Nov 13 00:13 tests.py
drwxr-xr-x  9 keshavkummari  staff  288 Nov 13 00:13 .
drwxr-xr-x  3 keshavkummari  staff   96 Nov 13 00:13 migrations

Step-9 : Write your first view :

home/views.py

$ cat views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><body bgcolor='#FFC300'><h1>Welcome to Django World</h1></body></html>")

This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the home directory, create a file called urls.py.


In the home/urls.py file include the following code:

$ pwd
/Users/keshavkummari/kkummari/home
$ cat urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index')
]



The next step is to point the root URLconf at the polls.urls module. In kkummari/urls.py,
add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:

$ pwd
/Users/keshavkummari/kkummari/kkummari
$ cat urls.py
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home/', include('home.urls')),
    url(r'^admin/', admin.site.urls),
]
$


Step-10 : Start the Web server :

$ python manage.py runserver


Step-11 : Creating an admin user :
First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser


$ python manage.py createsuperuser
Username (leave blank to use 'keshavkummari'):
Email address: keshav.kummari@gmail.com
Password:
Password (again):
Superuser created successfully.


Step-11 : Start the development server
The Django admin site is activated by default. Let’s start the development server and explore it.

If the server is not running start it like so:

$ python manage.py runserver


#-----------------------------------------------------------#

#-----------------------------------------------------------#
