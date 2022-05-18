# Django Quick Notes

- The applications which will provide services over the web are called web applications.
- `django-admin` is a command line interface tool to handle django applications.
- `django-admin strartproject <projectname>` - to create a project

```python
<projectname>
    manage.py
    <projectname>
        __init__.py
        settings.py
        wsgi.py
        urls.py
```

- `__init__.py` - empty file, because of this file. python treats `<projectname>` subfolder as a package.
- `settings.py` - contains project related settings and configurations like installed applications, middleware & database configurations.
- `wsgi.py` - stands for **`web services gateway interface`**, will be useful in deploying application to online server / production server.
- `urls.py` - stores all url patterns in the project. we have to define unique url pattern for each view in the application.
- End users will use this url patterns to access the webpages / views.
- `manage.py` - it is the most commonly used python script in django. it is a command line utility to interact with django project in various ways like run development server, run tests, create migrations.
- `python/py manage.py runserver` - to run development server
- `python/py manage.py migrate` - to apply migrations
- `python/py manage.py startapp <appname>` - to create a django application
- django application runs on port 8000 by default `http://localhost:8000`
- we can change the port number as follows `python manage.py runserver 7777` now server will run on port 7777 and we can access it using address `http://localhost:7777`

```python
<projectname>
    manage.py
    db.sqlite3
    <projectname>
        __init__.py
        urls.py
        wsgi.py
        settings.py
    <appname>
        __init__.py
        apps.py
        admin.py
        models.py
        views.py
        tests.py
        <migrations>
            __init__.py
```

- `__init__.py` - blank python file, because of special name python treats this folder as a package.
- `apps.py` - stores / contains application specific configurations.
- `models.py` - will store application data models.
- `admin.py` - we can register our models in this files. django will use this models in django admin interface.
- `tests.py` - contains test functions to test our code.
- `views.py` - contains view functions that handles requests and returns required responses.
- migrations folder store database specific information related to models.
- the most important files in every django application are `views.py` and `models.py`

## Activities required for application development

- before starting working on the application, add application name to `settings.py` under `INSTALLED_APPS` list, so django aware about the application.

```python
settings.py
INSTALLED_APPS = [
    .....,
    .....,
    <appname>
]
```

- create views for application in views.py, views are responsible for preparing required response to the end user and
- views contain the business logic
- two types of views are available:
  - function based views
  - class based views

```python
from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1>Hello World</h1>')
```

- each view will be specified as one function in views.py
- in the above code snippet display is the name of the function which is nothing but one view.
- each view should take atleast one argument (request)
- each view should return HttpResponse object with our required response.
- define a url pattern for our view in urls.py

```python
from django.urls import path, include
from django.contrib import admin
from <appname> import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/', views.display)
]
```

```python
urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/admin',admin.site.urls)
]

views.py
from django.shortcuts import render
from django.http import HttpResponse

```

- in django it is legal / possible to define multiple urls for same view

## django templates and static files

- `__file__` - returns the name of file
- `os.path.abspath(__file__)` - returns the absolute path of the file from root directory
- `os.path_dirname(<abspath>)` - returns the immediate parent directory name of input path
- `os.path.join(<path_1>, <path_2>)` - joins path_2 to path_1 and returns it
- add `STATIC_DIR` to `STATICFILES_DIR` list
- always include `{% load static %}` after `<!DOCTYPE html>`

```html
<!-- how to use static files in html django -->
{% load static %}
<img src="{% static 'images/filename.png' %}" alt="some text" />
```
