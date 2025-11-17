from django.apps import AppConfig

#this is your app configuration class
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #it tells  Django to use custom config
    name = 'myapp'
#name of the django folder


from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):  #this function runs when django starts
        import myapp.signals #this loads your signals so djnago knows them
