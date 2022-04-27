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
- `admin.py` - will register applications models. django will use this models in django admin interface.
- `tests.py` - contains test functions to test our code.
- `views.py` - contains view functions that handles requests and returns required responses.
- migrations folder store database specific information related to models.
- the most important files in every django application are `views.py` and `models.py`
- before starting working on the application, add application name to `settings.py` under `INSTALLED_APPS` list

```python
settings.py
INSTALLED_APPS = [
    .....,
    .....,
    <appname>
]
```
