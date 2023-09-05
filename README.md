<img src="https://static.djangoproject.com/img/logos/django-logo-positive.png" alt="Django Logo" width="200px"/>

# Django-coreyschafer
CoreySchafer tutotial - Full Stack web app with Django



#### Install environment (PIPENV)
```
pipenv shell
```

#### Generate a requirements.txt file from Pipfile.lock

- with pipenv
 ```pipenv requirements > requirements.txt```


#### Django Commands

##### Run the server
```
python manage.py runserver
```

##### Create new Django project
```
django-admin startproject PROJECTNAME
```


##### Create an app folder
```
python manage.py start app APPNAME
```

##### Prepare Migration file e.g. 0001_initial.py
```
python manage.py makemigrations
```

##### Apply Migrations (create/delete tables)
```
python manage.py migrate
```

##### Show Sql Query for specific migration
```
python manage.py sqlmigrate APPNAME MIGRATION_NUMBER
```
e.g.
```
python manage.py sqlmigrate myapp 0001
```

##### Create an Admin User
```
python manage.py createsuperuser
```

##### Change Any User's Password
```
python manage.py changepassword
```

##### Collecting Static Files Into One Folder
```
python manage.py collectstatic
```

##### Show Django Python Shell
```
python manage.py shell
```
